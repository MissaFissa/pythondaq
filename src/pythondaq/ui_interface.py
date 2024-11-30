# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QToolBar, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(1239, 816)
        MainWindow.setMinimumSize(QSize(1239, 816))
        MainWindow.setMaximumSize(QSize(16777214, 16777215))
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: b;\n"
"border-color: black")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leftFrame = QFrame(self.centralwidget)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.877, fx:0.496786, fy:0.499, stop:0.507 dimgrey stop:0.674877 black)")
        self.verticalLayout_7 = QVBoxLayout(self.leftFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.inputsFrame = QFrame(self.leftFrame)
        self.inputsFrame.setObjectName(u"inputsFrame")
        self.inputsFrame.setAutoFillBackground(False)
        self.inputsFrame.setFrameShape(QFrame.Shape.Box)
        self.inputsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.inputsFrame.setLineWidth(3)
        self.inputsFrame.setMidLineWidth(2)
        self.verticalLayout_4 = QVBoxLayout(self.inputsFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.start_stop_iterationsFrame = QFrame(self.inputsFrame)
        self.start_stop_iterationsFrame.setObjectName(u"start_stop_iterationsFrame")
        self.start_stop_iterationsFrame.setAutoFillBackground(False)
        self.start_stop_iterationsFrame.setStyleSheet(u"background-color:  dimgrey\n"
"")
        self.start_stop_iterationsFrame.setFrameShape(QFrame.Shape.Box)
        self.start_stop_iterationsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.start_stop_iterationsFrame.setMidLineWidth(2)
        self.horizontalLayout_4 = QHBoxLayout(self.start_stop_iterationsFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.startBox = QFrame(self.start_stop_iterationsFrame)
        self.startBox.setObjectName(u"startBox")
        self.startBox.setMinimumSize(QSize(80, 60))
        self.startBox.setStyleSheet(u"background-color: dimgrey")
        self.startBox.setFrameShape(QFrame.Shape.Box)
        self.startBox.setFrameShadow(QFrame.Shadow.Raised)
        self.startBox.setLineWidth(1)
        self.startBox.setMidLineWidth(2)
        self.verticalLayout = QVBoxLayout(self.startBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.startLabel = QLabel(self.startBox)
        self.startLabel.setObjectName(u"startLabel")
        self.startLabel.setStyleSheet(u"color: white")

        self.verticalLayout.addWidget(self.startLabel)

        self.startSpinbox = QSpinBox(self.startBox)
        self.startSpinbox.setObjectName(u"startSpinbox")
        self.startSpinbox.setMinimumSize(QSize(60, 20))
        self.startSpinbox.setAutoFillBackground(True)
        self.startSpinbox.setStyleSheet(u"background-color: black; color: white")
        self.startSpinbox.setMaximum(1023)

        self.verticalLayout.addWidget(self.startSpinbox)


        self.horizontalLayout_4.addWidget(self.startBox)

        self.stopBox = QFrame(self.start_stop_iterationsFrame)
        self.stopBox.setObjectName(u"stopBox")
        self.stopBox.setMinimumSize(QSize(80, 60))
        self.stopBox.setStyleSheet(u"background-color: dimgrey")
        self.stopBox.setFrameShape(QFrame.Shape.Box)
        self.stopBox.setFrameShadow(QFrame.Shadow.Raised)
        self.stopBox.setMidLineWidth(2)
        self.verticalLayout_5 = QVBoxLayout(self.stopBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stopLabel = QLabel(self.stopBox)
        self.stopLabel.setObjectName(u"stopLabel")
        self.stopLabel.setStyleSheet(u"color: white")

        self.verticalLayout_5.addWidget(self.stopLabel)

        self.stopSpinbox = QSpinBox(self.stopBox)
        self.stopSpinbox.setObjectName(u"stopSpinbox")
        self.stopSpinbox.setMinimumSize(QSize(60, 20))
        self.stopSpinbox.setAutoFillBackground(True)
        self.stopSpinbox.setStyleSheet(u"background-color: black; color: white")
        self.stopSpinbox.setMaximum(1023)
        self.stopSpinbox.setValue(1023)

        self.verticalLayout_5.addWidget(self.stopSpinbox)


        self.horizontalLayout_4.addWidget(self.stopBox)

        self.iterations = QFrame(self.start_stop_iterationsFrame)
        self.iterations.setObjectName(u"iterations")
        self.iterations.setMinimumSize(QSize(0, 60))
        self.iterations.setAutoFillBackground(False)
        self.iterations.setStyleSheet(u"color: black; background-color: dimgrey")
        self.iterations.setFrameShape(QFrame.Shape.Box)
        self.iterations.setFrameShadow(QFrame.Shadow.Raised)
        self.iterations.setMidLineWidth(2)
        self.verticalLayout_3 = QVBoxLayout(self.iterations)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.iterationsLabel = QLabel(self.iterations)
        self.iterationsLabel.setObjectName(u"iterationsLabel")
        self.iterationsLabel.setStyleSheet(u"color: white")

        self.verticalLayout_3.addWidget(self.iterationsLabel)

        self.iterationsSpinbox = QSpinBox(self.iterations)
        self.iterationsSpinbox.setObjectName(u"iterationsSpinbox")
        self.iterationsSpinbox.setMinimumSize(QSize(30, 20))
        self.iterationsSpinbox.setAutoFillBackground(False)
        self.iterationsSpinbox.setStyleSheet(u"background-color: black; color: white")
        self.iterationsSpinbox.setMaximum(100)
        self.iterationsSpinbox.setValue(1)

        self.verticalLayout_3.addWidget(self.iterationsSpinbox)


        self.horizontalLayout_4.addWidget(self.iterations)


        self.verticalLayout_4.addWidget(self.start_stop_iterationsFrame)

        self.deviceFrame = QFrame(self.inputsFrame)
        self.deviceFrame.setObjectName(u"deviceFrame")
        self.deviceFrame.setStyleSheet(u"background-color:  dimgrey\n"
"")
        self.deviceFrame.setFrameShape(QFrame.Shape.Box)
        self.deviceFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.deviceFrame.setMidLineWidth(2)
        self.verticalLayout_2 = QVBoxLayout(self.deviceFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.deviceLabel = QLabel(self.deviceFrame)
        self.deviceLabel.setObjectName(u"deviceLabel")
        self.deviceLabel.setStyleSheet(u"color: white; background-color: dimgrey")

        self.verticalLayout_2.addWidget(self.deviceLabel)

        self.deviceComboBox = QComboBox(self.deviceFrame)
        self.deviceComboBox.setObjectName(u"deviceComboBox")
        self.deviceComboBox.setAutoFillBackground(False)
        self.deviceComboBox.setStyleSheet(u"background-color: black; color:white")

        self.verticalLayout_2.addWidget(self.deviceComboBox)


        self.verticalLayout_4.addWidget(self.deviceFrame)

        self.plotButton = QPushButton(self.inputsFrame)
        self.plotButton.setObjectName(u"plotButton")
        self.plotButton.setStyleSheet(u"color: white; background-color: dimgrey")

        self.verticalLayout_4.addWidget(self.plotButton)


        self.verticalLayout_7.addWidget(self.inputsFrame)

        self.imageFrame = QFrame(self.leftFrame)
        self.imageFrame.setObjectName(u"imageFrame")
        self.imageFrame.setMaximumSize(QSize(16777215, 16777215))
        self.imageFrame.setAutoFillBackground(False)
        self.imageFrame.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.877, fx:0.496786, fy:0.499, stop:0.507 dimgrey stop:0.674877 black)")
        self.imageFrame.setFrameShape(QFrame.Shape.Box)
        self.imageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.imageFrame.setLineWidth(3)
        self.imageFrame.setMidLineWidth(2)
        self.horizontalLayout_3 = QHBoxLayout(self.imageFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.imageLabel = QLabel(self.imageFrame)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setPixmap(QPixmap(u"../../gus2.jpg"))
        self.imageLabel.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.imageLabel)


        self.verticalLayout_7.addWidget(self.imageFrame)


        self.horizontalLayout_2.addWidget(self.leftFrame)

        self.plotFrame = QFrame(self.centralwidget)
        self.plotFrame.setObjectName(u"plotFrame")
        self.plotFrame.setEnabled(True)
        self.plotFrame.setMinimumSize(QSize(600, 600))
        self.plotFrame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.plotFrame.setAutoFillBackground(False)
        self.plotFrame.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.877, fx:0.496786, fy:0.499, stop:0.507 dodgerblue, stop:0.674877 rgba(0, 0, 0, 255))")
        self.plotFrame.setFrameShape(QFrame.Shape.Box)
        self.plotFrame.setFrameShadow(QFrame.Shadow.Sunken)
        self.plotFrame.setLineWidth(0)
        self.plotFrame.setMidLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.plotFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.plotWidget = PlotWidget(self.plotFrame)
        self.plotWidget.setObjectName(u"plotWidget")
        self.plotWidget.setMaximumSize(QSize(16777215, 16777215))
        self.plotWidget.setAutoFillBackground(True)
        self.plotWidget.setStyleSheet(u"background-color: black;\n"
"color: dodgerblue")
        self.plotWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.plotWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.plotWidget.setLineWidth(0)
        self.plotWidget.setMidLineWidth(0)

        self.verticalLayout_6.addWidget(self.plotWidget)

        self.progressBarFrame = QFrame(self.plotFrame)
        self.progressBarFrame.setObjectName(u"progressBarFrame")
        self.progressBarFrame.setMaximumSize(QSize(16777215, 16777215))
        self.progressBarFrame.setAutoFillBackground(False)
        self.progressBarFrame.setStyleSheet(u"background-color: b")
        self.progressBarFrame.setFrameShape(QFrame.Shape.Box)
        self.progressBarFrame.setFrameShadow(QFrame.Shadow.Sunken)
        self.progressBarFrame.setLineWidth(1)
        self.progressBarFrame.setMidLineWidth(2)
        self.horizontalLayout = QHBoxLayout(self.progressBarFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressBarLabel = QLabel(self.progressBarFrame)
        self.progressBarLabel.setObjectName(u"progressBarLabel")
        self.progressBarLabel.setAutoFillBackground(False)
        self.progressBarLabel.setStyleSheet(u"background-color: black; color: white")

        self.horizontalLayout.addWidget(self.progressBarLabel)

        self.progressBar = QProgressBar(self.progressBarFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	border: 2px grey;\n"
"	border-radius: 5px;\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));\n"
"	width: 0.5px;\n"
"	margin: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)

        self.horizontalLayout.addWidget(self.progressBar)


        self.verticalLayout_6.addWidget(self.progressBarFrame)


        self.horizontalLayout_2.addWidget(self.plotFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1239, 21))
        self.menuBar.setAutoFillBackground(False)
        self.menuBar.setStyleSheet(u"color: dodgerblue;\n"
"background-color: black;\n"
)
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(False)
        MainWindow.setMenuBar(self.menuBar)

        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
    
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMouseTracking(False)
        self.toolBar.setAcceptDrops(False)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setStyleSheet(u"color: b;\n"
"background-color: dodgerblue;\n"
)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(16, 16))
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GraphApp", None))
        self.startLabel.setText(QCoreApplication.translate("MainWindow", u"Start ", None))
        self.stopLabel.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.iterationsLabel.setText(QCoreApplication.translate("MainWindow", u"Iterations", None))
        self.deviceLabel.setText(QCoreApplication.translate("MainWindow", u"Devices", None))
        self.plotButton.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.imageLabel.setText("")
        self.progressBarLabel.setText(QCoreApplication.translate("MainWindow", u"Scan Progress", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

