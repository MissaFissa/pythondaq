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
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(1020, 715)
        MainWindow.setMinimumSize(QSize(800, 700))
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
        self.leftFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 dodgerblue, stop:0.34 black, stop:0.55 dodgerblue, stop:0.98 black, stop:0.99 black, stop:1 black)")
        self.verticalLayout_7 = QVBoxLayout(self.leftFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.inputsFrame = QFrame(self.leftFrame)
        self.inputsFrame.setObjectName(u"inputsFrame")
        self.inputsFrame.setAutoFillBackground(False)
        self.inputsFrame.setFrameShape(QFrame.Shape.Box)
        self.inputsFrame.setFrameShadow(QFrame.Shadow.Sunken)
        self.inputsFrame.setLineWidth(1)
        self.inputsFrame.setMidLineWidth(3)
        self.inputsFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 dodgerblue, stop:0.34 black, stop:0.55 dodgerblue, stop:0.98 black, stop:0.99 dodgerblue, stop:1 black)")
        self.verticalLayout_4 = QVBoxLayout(self.inputsFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.start_stop_iterationsFrame = QFrame(self.inputsFrame)
        self.start_stop_iterationsFrame.setObjectName(u"start_stop_iterationsFrame")
        self.start_stop_iterationsFrame.setAutoFillBackground(False)
        self.start_stop_iterationsFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 dodgerblue, stop:0.34 black, stop:0.55 dodgerblue, stop:0.98 black, stop:0.99 black, stop:1 black)")
        self.start_stop_iterationsFrame.setFrameShape(QFrame.Shape.Box)
        self.start_stop_iterationsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.start_stop_iterationsFrame.setMidLineWidth(2)
        self.horizontalLayout_4 = QHBoxLayout(self.start_stop_iterationsFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.startBox = QFrame(self.start_stop_iterationsFrame)
        self.startBox.setObjectName(u"startBox")
        self.startBox.setMinimumSize(QSize(80, 60))
        self.startBox.setStyleSheet(u"color: black; background-color: dimgrey")
        self.startBox.setFrameShape(QFrame.Shape.Box)
        self.startBox.setFrameShadow(QFrame.Shadow.Sunken)
        self.startBox.setLineWidth(1)
        self.startBox.setMidLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.startBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.startValueLabel = QLabel(self.startBox)
        self.startValueLabel.setMinimumHeight(18)
        self.startValueLabel.setObjectName(u"startValueLabel")
        self.startValueLabel.setStyleSheet(u"color: white; background-color: transparent")

        self.verticalLayout.addWidget(self.startValueLabel)

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
        self.stopBox.setStyleSheet(u"color: black; background-color: dimgrey")
        self.stopBox.setFrameShape(QFrame.Shape.Box)
        self.stopBox.setFrameShadow(QFrame.Shadow.Sunken)
        self.stopBox.setMidLineWidth(1)
        self.stopBox.setLineWidth(1)
        self.verticalLayout_5 = QVBoxLayout(self.stopBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stopValueLabel = QLabel(self.stopBox)
        self.stopValueLabel.setMinimumHeight(18)
        self.stopValueLabel.setObjectName(u"stopValueLabel")
        self.stopValueLabel.setStyleSheet(u"color: white; background-color: transparent")

        self.verticalLayout_5.addWidget(self.stopValueLabel)

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
        self.iterations.setFrameShadow(QFrame.Shadow.Sunken)
        self.iterations.setMidLineWidth(1)
        self.iterations.setLineWidth(1)
        
        self.verticalLayout_3 = QVBoxLayout(self.iterations)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.iterationsLabel = QLabel(self.iterations)
        self.iterationsLabel.setMinimumHeight(18)
        self.iterationsLabel.setObjectName(u"iterationsLabel")
        self.iterationsLabel.setStyleSheet(u"color: white; background-color: transparent")

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
        self.deviceLabel.setMinimumHeight(18)
        self.deviceLabel.setObjectName(u"deviceLabel")
        self.deviceLabel.setStyleSheet(u"color: white; background-color: dimgrey")

        self.verticalLayout_2.addWidget(self.deviceLabel)

        self.deviceComboBox = QComboBox(self.deviceFrame)
        self.deviceComboBox.setObjectName(u"deviceComboBox")
        self.deviceComboBox.setAutoFillBackground(False)
        self.deviceComboBox.setStyleSheet(u"background-color: black; color:white")

        self.verticalLayout_2.addWidget(self.deviceComboBox)


        self.verticalLayout_4.addWidget(self.deviceFrame)

        self.startStopFrame = QFrame(self.inputsFrame)
        self.startStopFrame.setObjectName(u"startStopFrame")
        self.startStopFrame.setAutoFillBackground(False)
        self.startStopFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 dodgerblue, stop:0.34 black, stop:0.55 dodgerblue, stop:0.98 black, stop:0.99 black, stop:1 black)")
        self.startStopFrame.setFrameShape(QFrame.Shape.Box)
        self.startStopFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.startStopFrame.setLineWidth(1)
        self.startStopFrame.setMidLineWidth(2)
        self.verticalLayout_8 = QVBoxLayout(self.startStopFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.startButton = QPushButton(self.startStopFrame)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setStyleSheet(u"color: white; background-color: dimgrey")

        self.verticalLayout_8.addWidget(self.startButton, 0, Qt.AlignmentFlag.AlignTop)

        self.stopButton = QPushButton(self.startStopFrame)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setStyleSheet(u"color: white; background-color: dimgrey")

        self.verticalLayout_8.addWidget(self.stopButton, 0, Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_4.addWidget(self.startStopFrame)


        self.verticalLayout_7.addWidget(self.inputsFrame)

        self.imageFrame = QFrame(self.leftFrame)
        self.imageFrame.setObjectName(u"imageFrame")
        self.imageFrame.setMaximumSize(QSize(16777215, 16777215))
        self.imageFrame.setAutoFillBackground(False)
        self.imageFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 dodgerblue, stop:0.34 black, stop:0.55 dodgerblue, stop:0.98 black, stop:0.99 dodgerblue, stop:1 black)")
        self.imageFrame.setFrameShape(QFrame.Shape.Box)
        self.imageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.imageFrame.setLineWidth(3)
        self.imageFrame.setMidLineWidth(2)
        self.verticalLayout_12 = QVBoxLayout(self.imageFrame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.RangesLabelFrame = QFrame(self.imageFrame)
        self.RangesLabelFrame.setObjectName(u"RangesLabelFrame")
        self.RangesLabelFrame.setStyleSheet(u"background-color:black")
        self.RangesLabelFrame.setFrameShape(QFrame.Shape.Box)
        self.RangesLabelFrame.setFrameShadow(QFrame.Shadow.Sunken)
        self.RangesLabelFrame.setLineWidth(1)
        self.RangesLabelFrame.setMidLineWidth(3)
        self.horizontalLayout_3 = QHBoxLayout(self.RangesLabelFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.RangesLabel = QLabel(self.RangesLabelFrame)
        self.RangesLabel.setObjectName(u"RangesLabel")

        self.horizontalLayout_3.addWidget(self.RangesLabel)

        self.horizontalSpacer = QSpacerItem(245, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_12.addWidget(self.RangesLabelFrame)

        self.x_yRangesFrame = QFrame(self.imageFrame)
        self.x_yRangesFrame.setObjectName(u"x_yRangesFrame")
        self.x_yRangesFrame.setStyleSheet(u"background-color:black")
        self.x_yRangesFrame.setFrameShape(QFrame.Shape.Box)
        self.x_yRangesFrame.setFrameShadow(QFrame.Shadow.Sunken)
        self.x_yRangesFrame.setMidLineWidth(3)
        self.x_yRangesFrame.setLineWidth(1)
        self.verticalLayout_11 = QVBoxLayout(self.x_yRangesFrame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.xRangeFrame = QFrame(self.x_yRangesFrame)
        self.xRangeFrame.setObjectName(u"xRangeFrame")
        self.xRangeFrame.setMinimumSize(QSize(301, 71))
        self.xRangeFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 dodgerblue, stop:0.34 black, stop:0.55 dodgerblue, stop:0.98 black, stop:0.99 dodgerblue, stop:1 black)")
        self.xRangeFrame.setFrameShape(QFrame.Shape.Box)
        self.xRangeFrame.setFrameShadow(QFrame.Shadow.Sunken)
        self.xRangeFrame.setMidLineWidth(3)
        self.xRangeFrame.setLineWidth(1)
        self.verticalLayout_9 = QVBoxLayout(self.xRangeFrame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.xRangeLabel = QLabel("", self.xRangeFrame)
        self.xRangeLabel.setObjectName(u"xRangeLabel")
        self.xRangeLabel.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_9.addWidget(self.xRangeLabel, 0,Qt.AlignmentFlag.AlignLeft)

        self.xRangeSlider = QSlider(self.xRangeFrame)
        self.xRangeSlider.setObjectName(u"xRangeSlider")
        self.xRangeSlider.setAutoFillBackground(False)
        self.xRangeSlider.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.xRangeSlider.setStyleSheet(u"\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid dodgerblue;\n"
"background-color: black;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: b;\n"
"border: 1px solid dodgerblue;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 dodgerblue, stop:1 dodgerblue);\n"
"border: 1px solid dodgerblue;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 red, stop:1 #ddd);\n"
""
                        "border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: b;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: dodgerblue;\n"
"border-color: dodgerblue;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: dodgerblue;\n"
"border: 1px solid dodgerblue;\n"
"border-radius: 4px;}")
        self.xRangeSlider.setOrientation(Qt.Orientation.Horizontal)
        self.verticalLayout_9.addWidget(self.xRangeSlider)


        self.verticalLayout_11.addWidget(self.xRangeFrame)

        self.yRangeFrame = QFrame(self.x_yRangesFrame)
        self.yRangeFrame.setObjectName(u"yRangeFrame")
        self.yRangeFrame.setMinimumSize(QSize(301, 71))
        self.yRangeFrame.setAutoFillBackground(False)
        self.yRangeFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 dodgerblue, stop:0.34 black, stop:0.55 dodgerblue, stop:0.98 black, stop:0.99 dodgerblue, stop:1 black)")
        self.yRangeFrame.setFrameShape(QFrame.Shape.Box)
        self.yRangeFrame.setFrameShadow(QFrame.Shadow.Sunken)
        self.yRangeFrame.setMidLineWidth(3)
        self.yRangeFrame.setLineWidth(1)
        self.verticalLayout_10 = QVBoxLayout(self.yRangeFrame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.yRangeLabel = QLabel("", self.yRangeFrame)
        self.yRangeLabel.setObjectName(u"yRangeLabel")
        self.yRangeLabel.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_10.addWidget(self.yRangeLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.yRangeSlider = QSlider(self.yRangeFrame)
        self.yRangeSlider.setObjectName(u"yRangeSlider")
        self.yRangeSlider.setAutoFillBackground(False)

        self.yRangeSlider.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.yRangeSlider.setStyleSheet(u"\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid dodgerblue;\n"
"background-color: black;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"

"\n"
"QSlider::add-page:horizontal {\n"
"background: b;\n"
"border: 1px solid dodgerblue;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 dodgerblue, stop:1 dodgerblue);\n"
"border: 1px solid dodgerblue;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 red, stop:1 #ddd);\n"
""
                        "border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: b;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: dodgerblue;\n"
"border-color: dodgerblue;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: dodgerblue;\n"
"border: 1px solid dodgerblue;\n"
"border-radius: 4px;}")
        self.yRangeSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_10.addWidget(self.yRangeSlider)


        self.verticalLayout_11.addWidget(self.yRangeFrame)


        self.verticalLayout_12.addWidget(self.x_yRangesFrame)


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
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.horizontalLayout.addWidget(self.progressBar)


        self.verticalLayout_6.addWidget(self.progressBarFrame)


        self.horizontalLayout_2.addWidget(self.plotFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1020, 21))
        self.menuBar.setAutoFillBackground(False)
        self.menuBar.setStyleSheet(u"color: dodgerblue;\n"
"background-color: black")
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
"background-color: dodgerblue")
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(16, 16))
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GraphApp", None))
        self.startValueLabel.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stopValueLabel.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.iterationsLabel.setText(QCoreApplication.translate("MainWindow", u"Iterations", None))
        self.deviceLabel.setText(QCoreApplication.translate("MainWindow", u"Devices", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.RangesLabel.setText(QCoreApplication.translate("MainWindow", u"Ranges", None))
        self.xRangeLabel.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.yRangeLabel.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.progressBarLabel.setText(QCoreApplication.translate("MainWindow", u"Scan Progress", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"Toolbar", None))
    # retranslateUi

