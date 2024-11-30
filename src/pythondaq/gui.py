import csv, sys, time
from pathlib import Path
import numpy as np
import pyqtgraph as pg
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
                               QStyle, QToolBar, QVBoxLayout, QWidget)

# from pythondaq.diode_experiment import DiodeExperiment, list_resources

from pythondaq.diode_experiment_test import DiodeExperiment, list_resources

from pythondaq.ui_interface import Ui_MainWindow

pg.setConfigOption("background", "k")
pg.setConfigOption("foreground", "w")

cwd = Path.cwd()

class UserInterface(QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.menuBar = QMenuBar()
        self.ui.menuBar.setGeometry(QRect(0, 0, 800, 37))

        saveButton = QAction("Save", self)
        saveButtonIconPath = cwd / "icons/saveIcon.png"
        icon = QIcon()
        icon.addPixmap(QPixmap(saveButtonIconPath))
        saveButton.setIcon(icon)

        saveButton.setStatusTip("Save data in csv file")
        saveButton.triggered.connect(self.save)

        self.ui.toolBar.addAction(saveButton)

        fileMenu = self.ui.menuBar.addMenu("File")

        saveAction = QAction("Save", self)

        saveAction.setShortcut("Ctrl+S")

        fileMenu.addAction(saveAction)

        saveAction.triggered.connect(self.save)

        # self.ui.plotButton.clicked.connect(self.plot)

        list_devices = self.devices()

        for device in list_devices:

            self.ui.deviceComboBox.addItem(device)

        self.n = 10

        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(self.n)

        self.ui.plotButton.clicked.connect(self.start_scan)

        self.plot_timer = QTimer()
        self.plot_timer.timeout.connect(self.plot)
        self.plot_timer.start(100)

        self.port = self.ui.deviceComboBox.currentText() 

        self.experiment = DiodeExperiment(port = self.port)

    def devices(self):
        """Print list of connected devices.
        """
        # return list_resources()
        return ["ASRL::SIMLED::INSTR"]

    def save(self):

        filepath, _ = QFileDialog.getSaveFileName(filter = "CSV files (*.csv)")    

        with open(f'{filepath}', 'w', newline = '') as csvfile:
        
            writer = csv.writer(csvfile)
            header = ['Mean voltages LED', 'Mean currents LED', 'Errors voltages', 'Errors currents']
            writer.writerow(header)

            for mean_voltage_LED, mean_current_LED, errors_voltages, errors_currents in zip(self.means_voltages, self.means_currents, self.errors_voltages, self.errors_currents):

                writer.writerow([mean_voltage_LED, mean_current_LED, errors_voltages, errors_currents])
        
            self.ui.statusBar.showMessage("The file has been saved...", 3000)

        if filepath == "":

            return

    def start_scan(self):
        """Starts a scanning process with specified parameters.
        """
        start_value = self.ui.startSpinbox.value()
        stop_value = self.ui.stopSpinbox.value()
        iterations = self.ui.iterationsSpinbox.value()

        self.experiment.start_scan(start = start_value, stop = stop_value, iterations = iterations)

    @Slot()
    def plot(self):

        self.ui.plotWidget.clear()
  
        self.ui.plotWidget.plot(self.experiment.means_voltages_list, self.experiment.means_currents_list, symbol = "o", symbolSize = 5, pen = None)

        self.ui.plotWidget.setLabel("bottom", "Mean voltages LED [V]")
        self.ui.plotWidget.setLabel("left", "Mean currents LED [A]")
        error_bars = pg.ErrorBarItem(x = np.array(self.experiment.means_voltages_list), y = np.array(self.experiment.means_currents_list), width = 2 * np.array(self.experiment.errors_voltages_list), height = 2 * np.array(self.experiment.errors_currents_list))
        self.ui.plotWidget.addItem(error_bars)
        self.ui.plotWidget.showGrid(x = True, y = True)
  
        # self.ui.plotWidget.clear()
  
        # start_value = self.ui.startSpinbox.value()
        # stop_value = self.ui.stopSpinbox.value()
        # iterations = self.ui.iterationsSpinbox.value()
        # port = self.ui.deviceComboBox.currentText() 
        
        # experiment = DiodeExperiment(port = port)

        # self.errors_voltages, self.errors_currents, self.means_voltages, self.means_currents, self.voltages_LED, self.currents_LED = experiment.scan(start = start_value, stop = stop_value, iterations = iterations)

        # self.ui.plotWidget.plot(self.means_voltages, self.means_currents, symbol = "o", symbolSize = 5, pen = None)

        # self.ui.plotWidget.setLabel("bottom", "Mean voltages LED [V]")
        # self.ui.plotWidget.setLabel("left", "Mean currents LED [A]")
        # error_bars = pg.ErrorBarItem(x = self.means_voltages, y = self.means_currents, width = 2 * self.errors_voltages, height = 2 * self.errors_currents)
        # self.ui.plotWidget.addItem(error_bars)
        # self.ui.plotWidget.showGrid(x = True, y = True)

def main():

    app = QApplication(sys.argv)
    ui = UserInterface()
    # ui.plot()
    ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":

    main()