import csv, sys
from pathlib import Path
import numpy as np
import pyqtgraph as pg
import pandas as pd
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl, Slot, QTimer)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform, QShortcut)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox,
                               QFileDialog, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QLineEdit, QMainWindow, QMenuBar,
                               QPushButton, QSizePolicy, QSpinBox, QStatusBar,
                               QStyle, QToolBar, QVBoxLayout, QWidget, QSlider)

from pythondaq.diode_experiment import DiodeExperiment, list_resources
from pythondaq.ui_interface import Ui_MainWindow

pg.setConfigOption("foreground", "w")
pg.setConfigOptions(antialias = True)

cwd = Path.cwd()

class UserInterface(QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.backgroundColor = "black"
        self.dataColor = "white"
        self.path = None

        fileMenu = self.ui.menuBar.addMenu("File")

        openAction = QAction("Open...", self)
        openAction.setStatusTip("Open a document")
        openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.open)
        fileMenu.addAction(openAction)

        saveAction = QAction("Save", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)
  
        saveAsAction = QAction("Save As...", self)
        saveAsAction.setShortcut("Shift+Ctrl+S")
        fileMenu.addAction(saveAsAction)
        saveAsAction.triggered.connect(self.saveAs)
        
        scanMenu = self.ui.menuBar.addMenu("Scan")
        runAction = QAction("Start", self)
        runAction.setShortcut("F5")
        scanMenu.addAction(runAction)
        runAction.triggered.connect(self.start_scan)

        stopAction = QAction("Stop", self)
        stopAction.setShortcut("Shift+F5")
        scanMenu.addAction(stopAction)
        stopAction.triggered.connect(self.stop_scan)

        pauseAction = QAction("Pause", self)
        pauseAction.setShortcut("F4")
        scanMenu.addAction(pauseAction)
        pauseAction.triggered.connect(self.pause_scan)

        resumeAction = QAction("Resume", self)
        resumeAction.setShortcut("Shift+F4")
        scanMenu.addAction(resumeAction)
        resumeAction.triggered.connect(self.resume_scan)

        saveAsButton = QAction("Save As...", self)
        saveAsButtonIconPath = cwd / "icons/saveIcon.png"
        saveAsIcon = QIcon()
        saveAsIcon.addPixmap(QPixmap(saveAsButtonIconPath))
        saveAsButton.setIcon(saveAsIcon)
        saveAsButton.setStatusTip("Save data in csv file")
        self.ui.toolBar.addAction(saveAsButton)
        saveAsButton.triggered.connect(self.saveAs)

        playButton = QAction("Start", self)
        playButtonIconPath = cwd / "icons/playIcon.png"
        playIcon = QIcon()
        playIcon.addPixmap(QPixmap(playButtonIconPath))
        playButton.setIcon(playIcon)
        playButton.setStatusTip("Start a scan")
        self.ui.toolBar.addAction(playButton)
        playButton.triggered.connect(self.start_scan)

        endButton = QAction("Stop", self)
        endButtonIconPath = cwd / "icons/stopIcon.png"
        endIcon = QIcon()
        endIcon.addPixmap(QPixmap(endButtonIconPath))
        endButton.setIcon(endIcon)
        endButton.setStatusTip("Stop scanning")
        self.ui.toolBar.addAction(endButton)
        endButton.triggered.connect(self.stop_scan)

        self.n = np.abs(self.ui.stopSpinbox.value() - self.ui.startSpinbox.value())

        self.ui.progressBar.setRange(0, self.n)

        self.ui.xRangeSlider.setRange(0, 50)
        self.ui.xRangeSlider.setValue(25)
        self.ui.xRangeSlider.setSingleStep(5)
        self.ui.xRangeLabel.setText(f"x: {self.ui.xRangeSlider.value() / 10}")
        self.ui.xRangeSlider.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.ui.xRangeSlider.valueChanged.connect(self.updateXRange)

        self.ui.yRangeSlider.setRange(0, 100)
        self.ui.yRangeSlider.setValue(50)
        self.ui.yRangeSlider.setSingleStep(5)
        self.ui.yRangeLabel.setText(f"y: {self.ui.yRangeSlider.value() / 10}")
        self.ui.yRangeSlider.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.ui.yRangeSlider.valueChanged.connect(self.updateYRange)

        self.ui.plotWidget.setLabel("bottom", "Mean voltages LED [V]")
        self.ui.plotWidget.setLabel("left", "Mean currents LED [mA]")
        self.ui.plotWidget.showGrid(x = True, y = True)
        self.ui.plotWidget.setXRange(0, self.ui.xRangeSlider.value() / 10)
        self.ui.plotWidget.setYRange(0, self.ui.yRangeSlider.value() / 10)

        self.ui.backgroundColourLineEdit.returnPressed.connect(self.updateBackgroundColor)
        self.ui.dataColourLineEdit.returnPressed.connect(self.updateDataColor)

        self.ui.startButton.clicked.connect(self.start_scan)
        self.ui.stopButton.clicked.connect(self.stop_scan)
        self.plot_timer = QTimer()
        self.plot_timer.timeout.connect(self.updatePlot)
        self.plot_timer.start(100)

        list_devices = self.devices()

        for device in list_devices:

            self.ui.deviceComboBox.addItem(device)

        self.port = self.ui.deviceComboBox.currentText() 

        self.experiment = DiodeExperiment(port = self.port)

    def devices(self):
        """Returns list of connected devices.
        """
        return ["ASRL::SIMLED::INSTR"]

    def save(self):

        if (self.path):

            with open(f'{self.path}', 'w', newline = '') as existing_csvfile:
        
                writer = csv.writer(existing_csvfile)
                header = ['Mean voltages LED [V]', 'Mean currents LED [mA]', 'Errors voltages', 'Errors currents']
                writer.writerow(header)

                for mean_voltage_LED, mean_current_LED, errors_voltages, errors_currents in zip(self.experiment.means_voltages, self.experiment.means_currents, self.experiment.errors_voltages, self.experiment.errors_currents):

                    writer.writerow([mean_voltage_LED, mean_current_LED, errors_voltages, errors_currents])
        
                self.ui.statusBar.showMessage(f"The file has been saved...", 3000)

        if not (self.path):

            return
        
    def saveAs(self):
        """Creates a csv file containing the means of the voltages and currents, along with their corresponding errors.
        """
        filepath, _ = QFileDialog.getSaveFileName(filter = "CSV files (*.csv)")    
      
        if not filepath:

            return

        self.path = Path(filepath)

        with open(f'{filepath}', 'w', newline = '') as csvfile:
        
            writer = csv.writer(csvfile)
            header = ['Mean voltages LED [V]', 'Mean currents LED [mA]', 'Errors voltages', 'Errors currents']
            writer.writerow(header)

            for mean_voltage_LED, mean_current_LED, errors_voltages, errors_currents in zip(self.experiment.means_voltages, self.experiment.means_currents, self.experiment.errors_voltages, self.experiment.errors_currents):

                writer.writerow([mean_voltage_LED, mean_current_LED, errors_voltages, errors_currents])
        
            self.ui.statusBar.showMessage(f"The file has been saved as {self.path}...", 3000)

    def open(self):

        filename, _ = QFileDialog.getOpenFileName(filter = "CSV files (*.csv)")

        if filename:
            
            self.path = Path(filename)
            df = pd.read_csv(self.path)

            pd.to_numeric(df['Mean voltages LED [V]'], errors = 'coerce').notna()
            pd.to_numeric(df['Mean currents LED [mA]'], errors = 'coerce').notna()
            pd.to_numeric(df['Errors voltages'], errors = 'coerce').notna()
            pd.to_numeric(df['Errors currents'], errors = 'coerce').notna()

            df['means_voltages'] = df['Mean voltages LED [V]'].astype(float)
            df['means_currents'] = df['Mean currents LED [mA]'].astype(float)
            df['errors_voltages'] = df['Errors voltages'].astype(float)
            df['errors_currents'] = df['Errors currents'].astype(float)

            means_voltages = df['means_voltages'].tolist()
            means_currents = df['means_currents'].tolist()
            errors_voltages = df['errors_voltages'].tolist()
            errors_currents = df['errors_currents'].tolist()

            self.ui.plotWidget.clear()
    
            self.ui.plotWidget.plot(means_voltages, means_currents, symbol = "o", symbolSize = 5, pen = None)

            error_bars = pg.ErrorBarItem(x = np.array(means_voltages), y = np.array(means_currents), width = 2 * np.array(errors_voltages), height = 2 * np.array(errors_currents))
            self.ui.plotWidget.addItem(error_bars)
        
    @Slot()
    def start_scan(self):
        """Starts a scanning process with specified parameters.
        """
        self.ui.startButton.setEnabled(False)
        self.ui.stopButton.setEnabled(True)

        start_value = self.ui.startSpinbox.value()
        stop_value = self.ui.stopSpinbox.value()
        iterations = self.ui.iterationsSpinbox.value()

        self.experiment.start_scan(start = start_value, stop = stop_value, iterations = iterations)
        self.ui.statusBar.showMessage("Scan has been started...", 3000)

    @Slot()
    def stop_scan(self):
        """Stops a scanning process.
        """
        self.ui.startButton.setEnabled(True)
        self.ui.stopButton.setEnabled(False)

        self.experiment.stop_scan()
        self.ui.statusBar.showMessage("Scan has been stopped...", 3000)

    @Slot()
    def pause_scan(self):

        self.experiment.pause_scan()
        self.ui.statusBar.showMessage("Scan has been paused...", 3000)

    @Slot()
    def resume_scan(self):

        self.experiment.resume_scan()
        self.ui.statusBar.showMessage("Scan has been resumed...", 3000)

    def updateXRange(self, value):
        """Updates the xRangeLabel and XRange to the new value of the xRangeSlider.

        Args:
            value (int): updated value of the xRangeSlider.
        """
        self.ui.xRangeLabel.setText(f"x: {value / 10}")
        self.ui.plotWidget.setXRange(0, value / 10)

    def updateYRange(self, value):
        """Updates the yRangeLabel and YRange to the new value of the yRangeSlider.

        Args:
            value (int): updated value of the yRangeSlider.
        """
        self.ui.yRangeLabel.setText(f"y: {value / 10}")
        self.ui.plotWidget.setYRange(0, value / 10)

    def updateDataColor(self):
        
        self.dataColor = self.ui.dataColourLineEdit.text()
        self.ui.plotWidget.plot(self.experiment.means_voltages, self.experiment.means_currents, symbol = "o",  symbolPen = self.dataColor, symbolSize = 5, pen = None)

    def updateBackgroundColor(self):

        self.backgroundColor = self.ui.backgroundColourLineEdit.text()
        self.ui.plotWidget.setBackground(self.backgroundColor)

    @Slot()
    def updatePlot(self):
        """Updates the plotWidget when scan is running.
        """
        if self.experiment.is_scanning.is_set():
            
            if not self.experiment.pause.is_set():
                    
                self.ui.progressBar.setValue(self.experiment.counter)
                        
                self.ui.plotWidget.clear()
        
                self.ui.plotWidget.plot(self.experiment.means_voltages, self.experiment.means_currents, symbol = "o",  symbolPen = self.dataColor, symbolSize = 5, pen = None)

                error_bars = pg.ErrorBarItem(x = np.array(self.experiment.means_voltages), y = np.array(self.experiment.means_currents), width = 2 * np.array(self.experiment.errors_voltages), height = 2 * np.array(self.experiment.errors_currents))
                self.ui.plotWidget.addItem(error_bars)
            
                if self.ui.progressBar.value() == self.n:
                    
                    self.ui.statusBar.showMessage("Scan has been completed...", 3000)

def main():

    app = QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":

    main()