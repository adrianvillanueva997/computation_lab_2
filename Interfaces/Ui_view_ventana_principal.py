# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Proyecto Computacion 2\computation-lab-2\Interfaces\view_ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.table_proyectos = QtWidgets.QTableWidget(self.centralwidget)
        self.table_proyectos.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_proyectos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_proyectos.setObjectName("table_proyectos")
        self.table_proyectos.setColumnCount(4)
        self.table_proyectos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_proyectos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_proyectos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_proyectos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_proyectos.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.table_proyectos)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_Crear_proyecto = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Crear_proyecto.setObjectName("pushButton_Crear_proyecto")
        self.verticalLayout_3.addWidget(self.pushButton_Crear_proyecto)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout.addWidget(self.pushButton_back)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_Seleccionar_Proyecto = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Seleccionar_Proyecto.setObjectName("pushButton_Seleccionar_Proyecto")
        self.verticalLayout_4.addWidget(self.pushButton_Seleccionar_Proyecto)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proyectos"))
        item = self.table_proyectos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_proyectos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.table_proyectos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fecha creación"))
        item = self.table_proyectos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Clave invitacion"))
        self.pushButton_Crear_proyecto.setText(_translate("MainWindow", "Crear Proyecto"))
        self.pushButton_back.setText(_translate("MainWindow", "Atrás"))
        self.pushButton_Seleccionar_Proyecto.setText(_translate("MainWindow", "Seleccionar Proyecto"))
