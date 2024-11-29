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
        MainWindow.resize(799, 587)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: b;\n"
"border-color: black")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 231, 331))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: dimgray")
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(3)
        self.frame.setMidLineWidth(2)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.start_stop = QWidget(self.frame)
        self.start_stop.setObjectName(u"start_stop")
        self.start_stop.setAutoFillBackground(False)
        self.startbox = QFrame(self.start_stop)
        self.startbox.setObjectName(u"startbox")
        self.startbox.setGeometry(QRect(0, 0, 92, 76))
        self.startbox.setMinimumSize(QSize(80, 40))
        self.startbox.setFrameShape(QFrame.Shape.Box)
        self.startbox.setFrameShadow(QFrame.Shadow.Raised)
        self.startbox.setLineWidth(1)
        self.startbox.setMidLineWidth(2)
        self.verticalLayout = QVBoxLayout(self.startbox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.startLabel = QLabel(self.startbox)
        self.startLabel.setObjectName(u"startLabel")
        self.startLabel.setStyleSheet(u"color: white")

        self.verticalLayout.addWidget(self.startLabel)

        self.startSpinb = QSpinBox(self.startbox)
        self.startSpinb.setObjectName(u"startSpinb")
        self.startSpinb.setMinimumSize(QSize(60, 20))
        self.startSpinb.setAutoFillBackground(True)
        self.startSpinb.setStyleSheet(u"background-color: black; color: white")
        self.startSpinb.setMaximum(1023)

        self.verticalLayout.addWidget(self.startSpinb)

        self.stopbox = QFrame(self.start_stop)
        self.stopbox.setObjectName(u"stopbox")
        self.stopbox.setGeometry(QRect(100, 0, 92, 76))
        self.stopbox.setMinimumSize(QSize(80, 40))
        self.stopbox.setFrameShape(QFrame.Shape.Box)
        self.stopbox.setFrameShadow(QFrame.Shadow.Raised)
        self.stopbox.setMidLineWidth(2)
        self.verticalLayout_5 = QVBoxLayout(self.stopbox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stopLabel = QLabel(self.stopbox)
        self.stopLabel.setObjectName(u"stopLabel")
        self.stopLabel.setStyleSheet(u"color: white")

        self.verticalLayout_5.addWidget(self.stopLabel)

        self.stopSpinb = QSpinBox(self.stopbox)
        self.stopSpinb.setObjectName(u"stopSpinb")
        self.stopSpinb.setMinimumSize(QSize(60, 20))
        self.stopSpinb.setAutoFillBackground(True)
        self.stopSpinb.setStyleSheet(u"background-color: black; color: white")
        self.stopSpinb.setMaximum(1023)
        self.stopSpinb.setValue(1023)

        self.verticalLayout_5.addWidget(self.stopSpinb)


        self.verticalLayout_4.addWidget(self.start_stop)

        self.iterations = QFrame(self.frame)
        self.iterations.setObjectName(u"iterations")
        self.iterations.setAutoFillBackground(False)
        self.iterations.setStyleSheet(u"color: black")
        self.iterations.setFrameShape(QFrame.Shape.Box)
        self.iterations.setFrameShadow(QFrame.Shadow.Raised)
        self.iterations.setMidLineWidth(2)
        self.verticalLayout_3 = QVBoxLayout(self.iterations)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.itersLabel = QLabel(self.iterations)
        self.itersLabel.setObjectName(u"itersLabel")
        self.itersLabel.setStyleSheet(u"color: white")

        self.verticalLayout_3.addWidget(self.itersLabel)

        self.itersSpinb = QSpinBox(self.iterations)
        self.itersSpinb.setObjectName(u"itersSpinb")
        self.itersSpinb.setMinimumSize(QSize(30, 20))
        self.itersSpinb.setAutoFillBackground(False)
        self.itersSpinb.setStyleSheet(u"background-color: black; color: white")
        self.itersSpinb.setMaximum(100)
        self.itersSpinb.setValue(1)

        self.verticalLayout_3.addWidget(self.itersSpinb)


        self.verticalLayout_4.addWidget(self.iterations)

        self.device = QFrame(self.frame)
        self.device.setObjectName(u"device")
        self.device.setFrameShape(QFrame.Shape.Box)
        self.device.setFrameShadow(QFrame.Shadow.Raised)
        self.device.setMidLineWidth(2)
        self.verticalLayout_2 = QVBoxLayout(self.device)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.deviceLabel = QLabel(self.device)
        self.deviceLabel.setObjectName(u"deviceLabel")
        self.deviceLabel.setStyleSheet(u"color: white")

        self.verticalLayout_2.addWidget(self.deviceLabel)

        self.deviceCombo = QComboBox(self.device)
        self.deviceCombo.setObjectName(u"deviceCombo")
        self.deviceCombo.setAutoFillBackground(False)
        self.deviceCombo.setStyleSheet(u"background-color: black; color:white")

        self.verticalLayout_2.addWidget(self.deviceCombo)


        self.verticalLayout_4.addWidget(self.device)

        self.plotButton = QPushButton(self.frame)
        self.plotButton.setObjectName(u"plotButton")
        self.plotButton.setStyleSheet(u"color: white")

        self.verticalLayout_4.addWidget(self.plotButton)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QRect(230, 0, 561, 521))
        self.frame_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.877, fx:0.496786, fy:0.499, stop:0.507 dodgerblue, stop:0.674877 rgba(0, 0, 0, 255))")
        self.frame_2.setFrameShape(QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame_2.setLineWidth(0)
        self.frame_2.setMidLineWidth(0)
        self.plotWidget = PlotWidget(self.frame_2)
        self.plotWidget.setObjectName(u"plotWidget")
        self.plotWidget.setGeometry(QRect(10, 10, 551, 451))
        self.plotWidget.setContentsMargins(0, 0, 0, 0)
        self.plotWidget.setAutoFillBackground(True)
        self.plotWidget.setStyleSheet(u"background-color: black;\n"
"color: dodgerblue")
    
        self.horizontalFrame = QFrame(self.frame_2)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setGeometry(QRect(10, 470, 551, 52))
        self.horizontalFrame.setAutoFillBackground(False)
        self.horizontalFrame.setStyleSheet(u"background-color: b")
        self.horizontalFrame.setFrameShape(QFrame.Shape.Box)
        self.horizontalFrame.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalFrame.setLineWidth(1)
        self.horizontalFrame.setMidLineWidth(2)
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.horizontalFrame)
        self.label.setObjectName(u"label")
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: black; color: white")

        self.horizontalLayout.addWidget(self.label)

        self.progBar = QProgressBar(self.horizontalFrame)
        self.progBar.setObjectName(u"progBar")
        self.progBar.setEnabled(True)
        self.progBar.setStyleSheet(u"QProgressBar {\n"
"	border: 2px grey;\n"
"	border-radius: 5px;\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));\n"
"	width: 0.5px;\n"
"	margin: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.progBar.setValue(24)
        self.progBar.setTextVisible(False)

        self.horizontalLayout.addWidget(self.progBar)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 330, 231, 191))
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3.setLineWidth(3)
        self.frame_3.setMidLineWidth(2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 799, 21))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet(u"color: dodgerblue;\n"
"background-color: black")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
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
        self.startLabel.setText(QCoreApplication.translate("MainWindow", u"Start ", None))
        self.stopLabel.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.itersLabel.setText(QCoreApplication.translate("MainWindow", u"Iterations", None))
        self.deviceLabel.setText(QCoreApplication.translate("MainWindow", u"Devices", None))
        self.plotButton.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Scan Progress", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

