# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Proyecto Computacion 2\computation-lab-2\Interfaces\UI\view_modificar_usuario.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.gridLayout.addWidget(self.lineEdit_nombre, 0, 1, 1, 1)
        self.label_NombreUsuario = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_NombreUsuario.setFont(font)
        self.label_NombreUsuario.setObjectName("label_NombreUsuario")
        self.gridLayout.addWidget(self.label_NombreUsuario, 0, 0, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 2, 1, 1, 1)
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.gridLayout.addWidget(self.lineEdit_email, 1, 1, 1, 1)
        self.label_Password = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Password.setFont(font)
        self.label_Password.setObjectName("label_Password")
        self.gridLayout.addWidget(self.label_Password, 2, 0, 1, 1)
        self.label_Email = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Email.setFont(font)
        self.label_Email.setObjectName("label_Email")
        self.gridLayout.addWidget(self.label_Email, 1, 0, 1, 1)
        self.label_Rol = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Rol.setFont(font)
        self.label_Rol.setObjectName("label_Rol")
        self.gridLayout.addWidget(self.label_Rol, 3, 0, 1, 1)
        self.lineEdit_Rol = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Rol.setObjectName("lineEdit_Rol")
        self.gridLayout.addWidget(self.lineEdit_Rol, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Aceptar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Aceptar.setFont(font)
        self.pushButton_Aceptar.setObjectName("pushButton_Aceptar")
        self.horizontalLayout.addWidget(self.pushButton_Aceptar)
        self.pushButton_Cancelar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Cancelar.setFont(font)
        self.pushButton_Cancelar.setObjectName("pushButton_Cancelar")
        self.horizontalLayout.addWidget(self.pushButton_Cancelar)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modificar usuario"))
        self.label_NombreUsuario.setText(_translate("MainWindow", "Nombre Usuario"))
        self.label_Password.setText(_translate("MainWindow", "Password"))
        self.label_Email.setText(_translate("MainWindow", "Email"))
        self.label_Rol.setText(_translate("MainWindow", "Rol"))
        self.pushButton_Aceptar.setText(_translate("MainWindow", "Aceptar"))
        self.pushButton_Cancelar.setText(_translate("MainWindow", "Cancelar"))
