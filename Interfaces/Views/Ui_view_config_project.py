# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Proyecto Computacion 2\computation-lab-2\Interfaces\UI\view_config_project.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(306, 275)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_generarInvitacion = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_generarInvitacion.setFont(font)
        self.pushButton_generarInvitacion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_generarInvitacion.setObjectName("pushButton_generarInvitacion")
        self.verticalLayout.addWidget(self.pushButton_generarInvitacion)
        self.pushButton_detallesProyecto = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_detallesProyecto.setFont(font)
        self.pushButton_detallesProyecto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_detallesProyecto.setObjectName("pushButton_detallesProyecto")
        self.verticalLayout.addWidget(self.pushButton_detallesProyecto)
        self.pushButton_GestionarEtiquetas = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GestionarEtiquetas.setFont(font)
        self.pushButton_GestionarEtiquetas.setObjectName("pushButton_GestionarEtiquetas")
        self.verticalLayout.addWidget(self.pushButton_GestionarEtiquetas)
        self.pushButton_eliminarProyecto = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_eliminarProyecto.setFont(font)
        self.pushButton_eliminarProyecto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_eliminarProyecto.setObjectName("pushButton_eliminarProyecto")
        self.verticalLayout.addWidget(self.pushButton_eliminarProyecto)
        self.pushButton_Atras = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Atras.setFont(font)
        self.pushButton_Atras.setObjectName("pushButton_Atras")
        self.verticalLayout.addWidget(self.pushButton_Atras)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 306, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Configuración Proyecto"))
        self.pushButton_generarInvitacion.setText(_translate("MainWindow", "Generar invitación"))
        self.pushButton_detallesProyecto.setText(_translate("MainWindow", "Detalles del proyecto"))
        self.pushButton_GestionarEtiquetas.setText(_translate("MainWindow", "Gestionar etiquetas"))
        self.pushButton_eliminarProyecto.setText(_translate("MainWindow", "Eliminar proyecto"))
        self.pushButton_Atras.setText(_translate("MainWindow", "Atrás"))

