# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Proyecto Computacion 2\computation-lab-2\Interfaces\UI\view_menu_seleccion.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 599)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_Atras = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Atras.setFont(font)
        self.pushButton_Atras.setObjectName("pushButton_Atras")
        self.gridLayout.addWidget(self.pushButton_Atras, 6, 0, 1, 1)
        self.pushButton_ConfiguracionProyecto = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_ConfiguracionProyecto.setFont(font)
        self.pushButton_ConfiguracionProyecto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_ConfiguracionProyecto.setObjectName("pushButton_ConfiguracionProyecto")
        self.gridLayout.addWidget(self.pushButton_ConfiguracionProyecto, 5, 0, 1, 1)
        self.pushButton_VisualizacionDatos = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_VisualizacionDatos.setFont(font)
        self.pushButton_VisualizacionDatos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_VisualizacionDatos.setObjectName("pushButton_VisualizacionDatos")
        self.gridLayout.addWidget(self.pushButton_VisualizacionDatos, 1, 0, 1, 1)
        self.pushButton_CargarDatos = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_CargarDatos.setFont(font)
        self.pushButton_CargarDatos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_CargarDatos.setObjectName("pushButton_CargarDatos")
        self.gridLayout.addWidget(self.pushButton_CargarDatos, 0, 0, 1, 1)
        self.pushButton_Clasificacion = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Clasificacion.setFont(font)
        self.pushButton_Clasificacion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Clasificacion.setObjectName("pushButton_Clasificacion")
        self.gridLayout.addWidget(self.pushButton_Clasificacion, 3, 0, 1, 1)
        self.pushButton_Entrenar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Entrenar.setFont(font)
        self.pushButton_Entrenar.setObjectName("pushButton_Entrenar")
        self.gridLayout.addWidget(self.pushButton_Entrenar, 2, 0, 1, 1)
        self.pushButton_AnalisisSentimiento = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_AnalisisSentimiento.setFont(font)
        self.pushButton_AnalisisSentimiento.setObjectName("pushButton_AnalisisSentimiento")
        self.gridLayout.addWidget(self.pushButton_AnalisisSentimiento, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menú Proyecto"))
        self.pushButton_Atras.setText(_translate("MainWindow", "Atrás"))
        self.pushButton_ConfiguracionProyecto.setText(_translate("MainWindow", "Configuración de proyecto"))
        self.pushButton_VisualizacionDatos.setText(_translate("MainWindow", "Visualización de datos"))
        self.pushButton_CargarDatos.setText(_translate("MainWindow", "Cargar datos"))
        self.pushButton_Clasificacion.setText(_translate("MainWindow", "Clasificación"))
        self.pushButton_Entrenar.setText(_translate("MainWindow", "Entrenar"))
        self.pushButton_AnalisisSentimiento.setText(_translate("MainWindow", "Análisis de sentimiento"))
