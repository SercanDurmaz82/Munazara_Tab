# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Sercan/PycharmProjects/Eski Projeler/tab ama pyqt5/Takim_Ekle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Takim_Ekle(object):
    def setupUi(self, Takim_Ekle):
        Takim_Ekle.setObjectName("Takim_Ekle")
        Takim_Ekle.resize(566, 326)
        self.Kaydet = QtWidgets.QPushButton(Takim_Ekle)
        self.Kaydet.setGeometry(QtCore.QRect(190, 250, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Kaydet.setFont(font)
        self.Kaydet.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Kaydet.setIconSize(QtCore.QSize(40, 40))
        self.Kaydet.setObjectName("Kaydet")
        self.lineEdit = QtWidgets.QLineEdit(Takim_Ekle)
        self.lineEdit.setGeometry(QtCore.QRect(200, 80, 311, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Takim_Ekle)
        self.label.setGeometry(QtCore.QRect(10, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Takim_Ekle)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Takim_Ekle)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Takim_Ekle)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 210, 311, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Takim_Ekle)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 140, 311, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Takim_Ekle)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(Takim_Ekle)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 20, 311, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Takim_Ekle)
        QtCore.QMetaObject.connectSlotsByName(Takim_Ekle)

    def retranslateUi(self, Takim_Ekle):
        _translate = QtCore.QCoreApplication.translate
        Takim_Ekle.setWindowTitle(_translate("Takim_Ekle", "Takım Ekle"))
        self.Kaydet.setText(_translate("Takim_Ekle", "Kaydet"))
        self.label.setText(_translate("Takim_Ekle", "Takım İsmi"))
        self.label_2.setText(_translate("Takim_Ekle", "Birinci Konuşmacı"))
        self.label_3.setText(_translate("Takim_Ekle", "İkinci Konuşmacı"))
        self.label_4.setText(_translate("Takim_Ekle", "Üni İsmi"))

