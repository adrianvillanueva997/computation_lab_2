# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Proyecto Computacion 2\computation-lab-2\Interfaces\UI\view_resultados_entrenamiento.ui'
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
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_descartar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_descartar.setObjectName("pushButton_descartar")
        self.gridLayout.addWidget(self.pushButton_descartar, 4, 1, 1, 1)
        self.pushButton_guardarModelo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_guardarModelo.setObjectName("pushButton_guardarModelo")
        self.gridLayout.addWidget(self.pushButton_guardarModelo, 4, 0, 1, 1)
        self.label_matriz_place = QtWidgets.QLabel(self.centralwidget)
        self.label_matriz_place.setObjectName("label_matriz_place")
        self.gridLayout.addWidget(self.label_matriz_place, 1, 0, 1, 1)
        self.label_cross_place = QtWidgets.QLabel(self.centralwidget)
        self.label_cross_place.setObjectName("label_cross_place")
        self.gridLayout.addWidget(self.label_cross_place, 1, 1, 1, 1)
        self.label_nombremodelo = QtWidgets.QLabel(self.centralwidget)
        self.label_nombremodelo.setObjectName("label_nombremodelo")
        self.gridLayout.addWidget(self.label_nombremodelo, 3, 0, 1, 1)
        self.label_matrizconfusion = QtWidgets.QLabel(self.centralwidget)
        self.label_matrizconfusion.setObjectName("label_matrizconfusion")
        self.gridLayout.addWidget(self.label_matrizconfusion, 0, 0, 1, 1)
        self.label_crossvalidation = QtWidgets.QLabel(self.centralwidget)
        self.label_crossvalidation.setObjectName("label_crossvalidation")
        self.gridLayout.addWidget(self.label_crossvalidation, 0, 1, 1, 1)
        self.lineEdit_nombremodelo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nombremodelo.setObjectName("lineEdit_nombremodelo")
        self.gridLayout.addWidget(self.lineEdit_nombremodelo, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
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
        self.pushButton_descartar.setText(_translate("MainWindow", "Descartar"))
        self.pushButton_guardarModelo.setText(_translate("MainWindow", "Guardar Modelo"))
        self.label_matriz_place.setText(_translate("MainWindow", "Matriz_place"))
        self.label_cross_place.setText(_translate("MainWindow", "Cross_place"))
        self.label_nombremodelo.setText(_translate("MainWindow", "Nombre del modelo"))
        self.label_matrizconfusion.setText(_translate("MainWindow", "Matriz de confusión"))
        self.label_crossvalidation.setText(_translate("MainWindow", "Cross Validation"))

