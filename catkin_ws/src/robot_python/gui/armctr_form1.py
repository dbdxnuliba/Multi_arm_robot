# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'armctr_form1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ArmctrForm1(object):
    def setupUi(self, ArmctrForm1):
        ArmctrForm1.setObjectName("ArmctrForm1")
        ArmctrForm1.resize(1238, 903)
        ArmctrForm1.setIconSize(QtCore.QSize(16, 16))
        ArmctrForm1.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(ArmctrForm1)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 271))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 280, 451, 291))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(460, 480, 511, 351))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame = QtWidgets.QFrame(self.horizontalLayoutWidget_5)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 471, 221))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(180, 0, 131, 31))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(70, 270, 411, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(20, 270, 51, 31))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.frame)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(460, 10, 511, 471))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.horizontalLayoutWidget_6)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit_qq_armt = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_qq_armt.setGeometry(QtCore.QRect(80, 230, 401, 41))
        self.lineEdit_qq_armt.setObjectName("lineEdit_qq_armt")
        self.lineEdit_path = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_path.setGeometry(QtCore.QRect(10, 330, 471, 41))
        self.lineEdit_path.setText("")
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.label_32 = QtWidgets.QLabel(self.frame_4)
        self.label_32.setGeometry(QtCore.QRect(10, 280, 71, 33))
        self.label_32.setObjectName("label_32")
        self.lineEdit_qq_armc = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_qq_armc.setGeometry(QtCore.QRect(80, 280, 401, 41))
        self.lineEdit_qq_armc.setObjectName("lineEdit_qq_armc")
        self.label_31 = QtWidgets.QLabel(self.frame_4)
        self.label_31.setGeometry(QtCore.QRect(10, 230, 71, 33))
        self.label_31.setObjectName("label_31")
        self.lineEdit_f_armt = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_f_armt.setGeometry(QtCore.QRect(80, 80, 401, 41))
        self.lineEdit_f_armt.setObjectName("lineEdit_f_armt")
        self.lineEdit_f_armc = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_f_armc.setGeometry(QtCore.QRect(80, 130, 401, 41))
        self.lineEdit_f_armc.setObjectName("lineEdit_f_armc")
        self.label_33 = QtWidgets.QLabel(self.frame_4)
        self.label_33.setGeometry(QtCore.QRect(10, 80, 71, 33))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame_4)
        self.label_34.setGeometry(QtCore.QRect(10, 130, 61, 33))
        self.label_34.setObjectName("label_34")
        self.label_19 = QtWidgets.QLabel(self.frame_4)
        self.label_19.setGeometry(QtCore.QRect(230, 0, 81, 31))
        self.label_19.setObjectName("label_19")
        self.button_read = QtWidgets.QPushButton(self.frame_4)
        self.button_read.setGeometry(QtCore.QRect(20, 390, 111, 51))
        self.button_read.setAutoDefault(True)
        self.button_read.setObjectName("button_read")
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setGeometry(QtCore.QRect(150, 380, 331, 71))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_18 = QtWidgets.QLabel(self.frame_2)
        self.label_18.setGeometry(QtCore.QRect(100, 0, 151, 21))
        self.label_18.setObjectName("label_18")
        self.radioButton_armt = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_armt.setGeometry(QtCore.QRect(100, 30, 61, 25))
        self.radioButton_armt.setObjectName("radioButton_armt")
        self.radioButton_armc = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_armc.setGeometry(QtCore.QRect(180, 30, 61, 25))
        self.radioButton_armc.setObjectName("radioButton_armc")
        self.radioButton_all = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_all.setGeometry(QtCore.QRect(260, 30, 51, 25))
        self.radioButton_all.setChecked(True)
        self.radioButton_all.setObjectName("radioButton_all")
        self.radioButton_armr = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_armr.setGeometry(QtCore.QRect(20, 30, 61, 25))
        self.radioButton_armr.setObjectName("radioButton_armr")
        self.lineEdit_f_armr = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_f_armr.setGeometry(QtCore.QRect(80, 30, 401, 41))
        self.lineEdit_f_armr.setObjectName("lineEdit_f_armr")
        self.label_35 = QtWidgets.QLabel(self.frame_4)
        self.label_35.setGeometry(QtCore.QRect(10, 30, 61, 33))
        self.label_35.setObjectName("label_35")
        self.lineEdit_qq_armr = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_qq_armr.setGeometry(QtCore.QRect(80, 180, 401, 41))
        self.lineEdit_qq_armr.setObjectName("lineEdit_qq_armr")
        self.label_36 = QtWidgets.QLabel(self.frame_4)
        self.label_36.setGeometry(QtCore.QRect(10, 180, 71, 33))
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_6.addWidget(self.frame_4)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(970, 480, 261, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_6 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setGeometry(QtCore.QRect(70, 10, 111, 31))
        self.label_3.setObjectName("label_3")
        self.button_plan_init = QtWidgets.QPushButton(self.frame_6)
        self.button_plan_init.setGeometry(QtCore.QRect(20, 50, 211, 61))
        self.button_plan_init.setAutoDefault(True)
        self.button_plan_init.setObjectName("button_plan_init")
        self.button_plan_data = QtWidgets.QPushButton(self.frame_6)
        self.button_plan_data.setGeometry(QtCore.QRect(20, 140, 211, 61))
        self.button_plan_data.setAutoDefault(True)
        self.button_plan_data.setObjectName("button_plan_data")
        self.button_plan_home = QtWidgets.QPushButton(self.frame_6)
        self.button_plan_home.setGeometry(QtCore.QRect(20, 230, 211, 61))
        self.button_plan_home.setAutoDefault(True)
        self.button_plan_home.setObjectName("button_plan_home")
        self.verticalLayout.addWidget(self.frame_6)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(970, 10, 261, 471))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.button_begin = QtWidgets.QPushButton(self.frame_5)
        self.button_begin.setGeometry(QtCore.QRect(10, 20, 221, 61))
        self.button_begin.setIconSize(QtCore.QSize(16, 16))
        self.button_begin.setAutoRepeat(False)
        self.button_begin.setAutoExclusive(False)
        self.button_begin.setAutoRepeatDelay(400)
        self.button_begin.setAutoRepeatInterval(200)
        self.button_begin.setAutoDefault(True)
        self.button_begin.setFlat(False)
        self.button_begin.setObjectName("button_begin")
        self.button_stop = QtWidgets.QPushButton(self.frame_5)
        self.button_stop.setGeometry(QtCore.QRect(10, 110, 221, 61))
        self.button_stop.setAutoDefault(True)
        self.button_stop.setObjectName("button_stop")
        self.button_receive = QtWidgets.QPushButton(self.frame_5)
        self.button_receive.setGeometry(QtCore.QRect(40, 380, 161, 61))
        self.button_receive.setAutoDefault(True)
        self.button_receive.setObjectName("button_receive")
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setGeometry(QtCore.QRect(10, 210, 219, 131))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.checkBox_imp = QtWidgets.QCheckBox(self.frame_8)
        self.checkBox_imp.setGeometry(QtCore.QRect(30, 50, 161, 21))
        self.checkBox_imp.setObjectName("checkBox_imp")
        self.checkBox_force = QtWidgets.QCheckBox(self.frame_8)
        self.checkBox_force.setGeometry(QtCore.QRect(30, 90, 161, 21))
        self.checkBox_force.setObjectName("checkBox_force")
        self.checkBox_real = QtWidgets.QCheckBox(self.frame_8)
        self.checkBox_real.setGeometry(QtCore.QRect(30, 10, 161, 22))
        self.checkBox_real.setObjectName("checkBox_real")
        self.button_begin.raise_()
        self.button_stop.raise_()
        self.button_receive.raise_()
        self.lineEdit_f_armr.raise_()
        self.label_35.raise_()
        self.frame_8.raise_()
        self.verticalLayout_2.addWidget(self.frame_5)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 570, 451, 261))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        ArmctrForm1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ArmctrForm1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1238, 31))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        ArmctrForm1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ArmctrForm1)
        self.statusbar.setObjectName("statusbar")
        ArmctrForm1.setStatusBar(self.statusbar)

        self.retranslateUi(ArmctrForm1)
        QtCore.QMetaObject.connectSlotsByName(ArmctrForm1)

    def retranslateUi(self, ArmctrForm1):
        _translate = QtCore.QCoreApplication.translate
        ArmctrForm1.setWindowTitle(_translate("ArmctrForm1", "MainWindow"))
        self.label.setText(_translate("ArmctrForm1", "?????????????????????"))
        self.label_15.setText(_translate("ArmctrForm1", "?????????"))
        self.lineEdit_qq_armt.setText(_translate("ArmctrForm1", "/home/d/catkin_ws/src/robot_python/data/robots/armctr/armt_position.txt"))
        self.label_32.setText(_translate("ArmctrForm1", "qq_armc:"))
        self.lineEdit_qq_armc.setText(_translate("ArmctrForm1", "/home/d/catkin_ws/src/robot_python/data/robots/armctr/armc_position.txt"))
        self.label_31.setText(_translate("ArmctrForm1", "qq_armt:"))
        self.lineEdit_f_armt.setText(_translate("ArmctrForm1", "/home/d/catkin_ws/src/robot_python/data/robots/armctr/armt_force.txt"))
        self.lineEdit_f_armc.setText(_translate("ArmctrForm1", "/home/d/catkin_ws/src/robot_python/data/robots/armctr/armc_force.txt"))
        self.label_33.setText(_translate("ArmctrForm1", "f_armt:"))
        self.label_34.setText(_translate("ArmctrForm1", "f_armc:"))
        self.label_19.setText(_translate("ArmctrForm1", "???????????????"))
        self.button_read.setText(_translate("ArmctrForm1", "????????????"))
        self.label_18.setText(_translate("ArmctrForm1", "????????????????????????"))
        self.radioButton_armt.setText(_translate("ArmctrForm1", "armt"))
        self.radioButton_armc.setText(_translate("ArmctrForm1", "armc"))
        self.radioButton_all.setText(_translate("ArmctrForm1", "all"))
        self.radioButton_armr.setText(_translate("ArmctrForm1", "armr"))
        self.lineEdit_f_armr.setText(_translate("ArmctrForm1", "/home/d/catkin_ws/src/robot_python/data/robots/armctr/armr_force.txt"))
        self.label_35.setText(_translate("ArmctrForm1", "f_armr:"))
        self.lineEdit_qq_armr.setText(_translate("ArmctrForm1", "/home/d/catkin_ws/src/robot_python/data/robots/armctr/armr_position.txt"))
        self.label_36.setText(_translate("ArmctrForm1", "qq_armr:"))
        self.label_3.setText(_translate("ArmctrForm1", "?????????????????????"))
        self.button_plan_init.setText(_translate("ArmctrForm1", "???????????????"))
        self.button_plan_data.setText(_translate("ArmctrForm1", "??????????????????"))
        self.button_plan_home.setText(_translate("ArmctrForm1", "???????????????"))
        self.button_begin.setText(_translate("ArmctrForm1", "??????"))
        self.button_stop.setText(_translate("ArmctrForm1", "??????"))
        self.button_receive.setText(_translate("ArmctrForm1", "?????????????????????"))
        self.checkBox_imp.setText(_translate("ArmctrForm1", "?????????    ????????????"))
        self.checkBox_force.setText(_translate("ArmctrForm1", "????????????    ????????????"))
        self.checkBox_real.setText(_translate("ArmctrForm1", "?????????    ????????????"))

