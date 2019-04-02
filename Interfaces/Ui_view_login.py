# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Proyecto Computacion 2\computation-lab-2\Interfaces\view_login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(348, 215)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 556))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.gridLayout.addWidget(self.label_password, 1, 0, 1, 1)
        self.boton_aceptar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.boton_aceptar.setFont(font)
        self.boton_aceptar.setDefault(True)
        self.boton_aceptar.setObjectName("boton_aceptar")
        self.gridLayout.addWidget(self.boton_aceptar, 2, 1, 1, 1)
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.gridLayout.addWidget(self.label_username, 0, 0, 1, 1)
        self.line_usuario = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.line_usuario.setFont(font)
        self.line_usuario.setObjectName("line_usuario")
        self.gridLayout.addWidget(self.line_usuario, 0, 1, 1, 1)
        self.line_password = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.line_password.setFont(font)
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setObjectName("line_password")
        self.gridLayout.addWidget(self.line_password, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.boton_aceptar.setText(_translate("MainWindow", "Aceptar"))
        self.label_username.setText(_translate("MainWindow", "Usuario"))

