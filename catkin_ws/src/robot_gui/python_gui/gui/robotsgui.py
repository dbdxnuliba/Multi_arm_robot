# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robotsgui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1238, 903)
        MainWindow.setIconSize(QtCore.QSize(16, 16))
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 391))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_v = QtWidgets.QLabel(self.frame_2)
        self.label_v.setGeometry(QtCore.QRect(140, 180, 89, 23))
        self.label_v.setObjectName("label_v")
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 410, 451, 421))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(480, 410, 481, 421))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame = QtWidgets.QFrame(self.horizontalLayoutWidget_5)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5.addWidget(self.frame)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(480, 10, 481, 391))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.horizontalLayoutWidget_6)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_4)
        self.lcdNumber.setGeometry(QtCore.QRect(151, 0, 321, 321))
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalSlider = QtWidgets.QSlider(self.frame_4)
        self.verticalSlider.setGeometry(QtCore.QRect(10, 0, 29, 321))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.progressBar = QtWidgets.QProgressBar(self.frame_4)
        self.progressBar.setGeometry(QtCore.QRect(10, 330, 471, 41))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_6.addWidget(self.frame_4)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(970, 410, 261, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_6 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setGeometry(QtCore.QRect(90, 0, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 191, 31))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 21, 33))
        self.label_4.setObjectName("label_4")
        self.lineEdit_b = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_b.setGeometry(QtCore.QRect(50, 250, 181, 33))
        self.lineEdit_b.setObjectName("lineEdit_b")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setGeometry(QtCore.QRect(20, 310, 21, 33))
        self.label_5.setObjectName("label_5")
        self.lineEdit_k = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_k.setGeometry(QtCore.QRect(50, 310, 181, 33))
        self.lineEdit_k.setObjectName("lineEdit_k")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setGeometry(QtCore.QRect(20, 360, 16, 33))
        self.label_6.setObjectName("label_6")
        self.lineEdit_i = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_i.setGeometry(QtCore.QRect(50, 360, 181, 33))
        self.lineEdit_i.setObjectName("lineEdit_i")
        self.lineEdit_m = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_m.setGeometry(QtCore.QRect(50, 190, 180, 33))
        self.lineEdit_m.setObjectName("lineEdit_m")
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        self.label_7.setGeometry(QtCore.QRect(20, 250, 21, 33))
        self.label_7.setObjectName("label_7")
        self.textEdit = QtWidgets.QTextEdit(self.frame_6)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 221, 81))
        self.textEdit.setObjectName("textEdit")
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        self.label_8.setGeometry(QtCore.QRect(10, 120, 31, 33))
        self.label_8.setObjectName("label_8")
        self.lineEdit_dir = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_dir.setGeometry(QtCore.QRect(40, 120, 191, 33))
        self.lineEdit_dir.setObjectName("lineEdit_dir")
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit_m.raise_()
        self.label_4.raise_()
        self.lineEdit_b.raise_()
        self.label_7.raise_()
        self.label_5.raise_()
        self.lineEdit_k.raise_()
        self.label_6.raise_()
        self.lineEdit_i.raise_()
        self.textEdit.raise_()
        self.label_8.raise_()
        self.lineEdit_dir.raise_()
        self.verticalLayout.addWidget(self.frame_6)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(970, 10, 261, 391))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.beginButton = QtWidgets.QPushButton(self.frame_5)
        self.beginButton.setGeometry(QtCore.QRect(10, 20, 221, 61))
        self.beginButton.setIconSize(QtCore.QSize(16, 16))
        self.beginButton.setAutoRepeat(False)
        self.beginButton.setAutoExclusive(False)
        self.beginButton.setAutoRepeatDelay(400)
        self.beginButton.setAutoRepeatInterval(200)
        self.beginButton.setAutoDefault(True)
        self.beginButton.setFlat(False)
        self.beginButton.setObjectName("beginButton")
        self.endbutton = QtWidgets.QPushButton(self.frame_5)
        self.endbutton.setGeometry(QtCore.QRect(10, 110, 221, 61))
        self.endbutton.setAutoDefault(True)
        self.endbutton.setObjectName("endbutton")
        self.readButton = QtWidgets.QPushButton(self.frame_5)
        self.readButton.setGeometry(QtCore.QRect(60, 210, 151, 51))
        self.readButton.setAutoDefault(True)
        self.readButton.setDefault(False)
        self.readButton.setObjectName("readButton")
        self.layoutWidget = QtWidgets.QWidget(self.frame_5)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 280, 181, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pubButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pubButton.setAutoDefault(True)
        self.pubButton.setObjectName("pubButton")
        self.verticalLayout_3.addWidget(self.pubButton)
        self.readDirButton = QtWidgets.QPushButton(self.layoutWidget)
        self.readDirButton.setAutoDefault(True)
        self.readDirButton.setObjectName("readDirButton")
        self.verticalLayout_3.addWidget(self.readDirButton)
        self.verticalLayout_2.addWidget(self.frame_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1238, 35))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_v.setText(_translate("MainWindow", "????????????"))
        self.label.setText(_translate("MainWindow", "????????????"))
        self.label_2.setText(_translate("MainWindow", "?????????????????????MBKI"))
        self.label_4.setText(_translate("MainWindow", "M:"))
        self.label_5.setText(_translate("MainWindow", "K:"))
        self.label_6.setText(_translate("MainWindow", "I:"))
        self.label_7.setText(_translate("MainWindow", "B:"))
        self.label_8.setText(_translate("MainWindow", "dir:"))
        self.beginButton.setText(_translate("MainWindow", "??????"))
        self.endbutton.setText(_translate("MainWindow", "??????"))
        self.readButton.setText(_translate("MainWindow", "??????MBKI??????"))
        self.pubButton.setText(_translate("MainWindow", "publisher"))
        self.readDirButton.setText(_translate("MainWindow", "get pub dir"))

