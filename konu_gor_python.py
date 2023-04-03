# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Sercan/PycharmProjects/Eski Projeler/tab ama pyqt5/konu_gor.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(984, 584)
        self.Info = QtWidgets.QPushButton(Form)
        self.Info.setGeometry(QtCore.QRect(50, 490, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.Info.setFont(font)
        self.Info.setObjectName("Info")
        self.Konu = QtWidgets.QPushButton(Form)
        self.Konu.setGeometry(QtCore.QRect(760, 490, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.Konu.setFont(font)
        self.Konu.setObjectName("Konu")
        self.Info_Gor = QtWidgets.QLabel(Form)
        self.Info_Gor.setGeometry(QtCore.QRect(10, 0, 941, 221))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.Info_Gor.setFont(font)
        self.Info_Gor.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Info_Gor.setText("")
        self.Info_Gor.setWordWrap(True)
        self.Info_Gor.setObjectName("Info_Gor")
        self.Konu_Gor = QtWidgets.QLabel(Form)
        self.Konu_Gor.setGeometry(QtCore.QRect(10, 230, 941, 251))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.Konu_Gor.setFont(font)
        self.Konu_Gor.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Konu_Gor.setText("")
        self.Konu_Gor.setWordWrap(True)
        self.Konu_Gor.setObjectName("Konu_Gor")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Info.setText(_translate("Form", "Info"))
        self.Konu.setText(_translate("Form", "Konu"))

