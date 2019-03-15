# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Proyecto Computacion 2\computation-lab-2\Interfaces\view_proyecto_cargar_proyecto.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(693, 522)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_Cancelar = QtWidgets.QGridLayout()
        self.gridLayout_Cancelar.setObjectName("gridLayout_Cancelar")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_Cancelar.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_Cancelar, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.gridLayout_Entrenar = QtWidgets.QGridLayout()
        self.gridLayout_Entrenar.setObjectName("gridLayout_Entrenar")
        self.pushButton_Cargar_Datos = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Cargar_Datos.setObjectName("pushButton_Cargar_Datos")
        self.gridLayout_Entrenar.addWidget(self.pushButton_Cargar_Datos, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_Entrenar.addItem(spacerItem1, 5, 0, 1, 1)
        self.pushButton_Entrenar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Entrenar.setObjectName("pushButton_Entrenar")
        self.gridLayout_Entrenar.addWidget(self.pushButton_Entrenar, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_Entrenar.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_Entrenar.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_Entrenar.addItem(spacerItem4, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_Entrenar, 0, 0, 3, 1)
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setObjectName("pushButton_back")
        self.gridLayout.addWidget(self.pushButton_back, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "Cancelar"))
        self.pushButton_Cargar_Datos.setText(_translate("MainWindow", "Cargar Datos"))
        self.pushButton_Entrenar.setText(_translate("MainWindow", "Entrenar"))
        self.pushButton_back.setText(_translate("MainWindow", "Atrás"))

