# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loggin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 556))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.line_usuario.setObjectName("line_usuario")
        self.gridLayout.addWidget(self.line_usuario, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.line_password = QtWidgets.QLineEdit(self.centralwidget)
        self.line_password.setObjectName("line_password")
        self.gridLayout.addWidget(self.line_password, 1, 1, 1, 1)
        self.boton_aceptar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_aceptar.setObjectName("boton_aceptar")
        self.gridLayout.addWidget(self.boton_aceptar, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.boton_aceptar.setText(_translate("MainWindow", "Aceptar"))

