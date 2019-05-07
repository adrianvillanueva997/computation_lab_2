# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Proyecto Computacion 2\computation-lab-2\Interfaces\UI\view_gestionar_etiquetas.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 451)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_etiquetas = QtWidgets.QLabel(self.centralwidget)
        self.label_etiquetas.setObjectName("label_etiquetas")
        self.gridLayout.addWidget(self.label_etiquetas, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 2)
        self.pushButton_eliminar_etiqueta = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_eliminar_etiqueta.setObjectName("pushButton_eliminar_etiqueta")
        self.gridLayout.addWidget(self.pushButton_eliminar_etiqueta, 4, 0, 1, 1)
        self.label_addlabel = QtWidgets.QLabel(self.centralwidget)
        self.label_addlabel.setObjectName("label_addlabel")
        self.gridLayout.addWidget(self.label_addlabel, 0, 0, 1, 1)
        self.pushButton_cerrar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cerrar.setObjectName("pushButton_cerrar")
        self.gridLayout.addWidget(self.pushButton_cerrar, 4, 2, 1, 1)
        self.pushButton_guardar_cambios = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_guardar_cambios.setObjectName("pushButton_guardar_cambios")
        self.gridLayout.addWidget(self.pushButton_guardar_cambios, 4, 1, 1, 1)
        self.lineEdit_nuevaetiqueta = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nuevaetiqueta.setObjectName("lineEdit_nuevaetiqueta")
        self.gridLayout.addWidget(self.lineEdit_nuevaetiqueta, 1, 0, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestionar etiquetas"))
        self.label_etiquetas.setText(_translate("MainWindow", "Etiquetas"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Etiqueta"))
        self.pushButton_eliminar_etiqueta.setText(_translate("MainWindow", "Eliminar etiqueta"))
        self.label_addlabel.setText(_translate("MainWindow", "Añadir etiqueta"))
        self.pushButton_cerrar.setText(_translate("MainWindow", "Cerrar"))
        self.pushButton_guardar_cambios.setText(_translate("MainWindow", "Guardar cambios"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
