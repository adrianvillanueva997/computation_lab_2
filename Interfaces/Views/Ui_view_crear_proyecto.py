# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Proyecto Computacion 2\computation-lab-2\Interfaces\UI\view_crear_proyecto.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(342, 452)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label_nombreproyecto = QtWidgets.QLabel(self.centralwidget)
        self.label_nombreproyecto.setObjectName("label_nombreproyecto")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_nombreproyecto)
        self.lineEdit_nombreProyecto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nombreProyecto.setObjectName("lineEdit_nombreProyecto")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_nombreProyecto)
        self.label_NuevaEtiqueta = QtWidgets.QLabel(self.centralwidget)
        self.label_NuevaEtiqueta.setObjectName("label_NuevaEtiqueta")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_NuevaEtiqueta)
        self.lineEdit_nuevaEtiqueta = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nuevaEtiqueta.setObjectName("lineEdit_nuevaEtiqueta")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_nuevaEtiqueta)
        self.label__Etiquetas = QtWidgets.QLabel(self.centralwidget)
        self.label__Etiquetas.setObjectName("label__Etiquetas")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label__Etiquetas)
        self.tableWidget_etiquetas = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_etiquetas.setObjectName("tableWidget_etiquetas")
        self.tableWidget_etiquetas.setColumnCount(1)
        self.tableWidget_etiquetas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_etiquetas.setHorizontalHeaderItem(0, item)
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.tableWidget_etiquetas)
        self.pushButton_aceptar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_aceptar.setEnabled(False)
        self.pushButton_aceptar.setObjectName("pushButton_aceptar")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.pushButton_aceptar)
        self.pushButton_cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancelar.setObjectName("pushButton_cancelar")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.pushButton_cancelar)
        self.pushButton_addlabel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addlabel.setObjectName("pushButton_addlabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pushButton_addlabel)
        self.pushButton_removelabel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_removelabel.setObjectName("pushButton_removelabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.pushButton_removelabel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 342, 31))
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
        self.label_nombreproyecto.setText(_translate("MainWindow", "Nombre del Proyecto"))
        self.label_NuevaEtiqueta.setText(_translate("MainWindow", "Nueva Etiqueta"))
        self.label__Etiquetas.setText(_translate("MainWindow", "Etiquetas"))
        item = self.tableWidget_etiquetas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Etiqueta"))
        self.pushButton_aceptar.setText(_translate("MainWindow", "Aceptar"))
        self.pushButton_cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.pushButton_addlabel.setText(_translate("MainWindow", "Añadir Etiqueta"))
        self.pushButton_removelabel.setText(_translate("MainWindow", "Eliminar etiqueta"))

