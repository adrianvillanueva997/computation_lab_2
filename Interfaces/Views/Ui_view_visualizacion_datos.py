# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Proyecto Computacion 2\computation-lab-2\Interfaces\UI\view_visualizacion_datos.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1193, 714)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget_reviews = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget_reviews.setFont(font)
        self.tableWidget_reviews.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_reviews.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_reviews.setObjectName("tableWidget_reviews")
        self.tableWidget_reviews.setColumnCount(8)
        self.tableWidget_reviews.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reviews.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reviews.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reviews.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reviews.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reviews.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reviews.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reviews.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reviews.setHorizontalHeaderItem(7, item)
        self.gridLayout.addWidget(self.tableWidget_reviews, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_filtro = QtWidgets.QLabel(self.centralwidget)
        self.label_filtro.setObjectName("label_filtro")
        self.horizontalLayout.addWidget(self.label_filtro)
        self.comboBox_filtro = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_filtro.setObjectName("comboBox_filtro")
        self.comboBox_filtro.addItem("")
        self.comboBox_filtro.addItem("")
        self.comboBox_filtro.addItem("")
        self.comboBox_filtro.addItem("")
        self.comboBox_filtro.addItem("")
        self.comboBox_filtro.addItem("")
        self.comboBox_filtro.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_filtro)
        self.lineEdit_filtro = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_filtro.setObjectName("lineEdit_filtro")
        self.horizontalLayout.addWidget(self.lineEdit_filtro)
        self.pushButton_applyfilter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_applyfilter.setObjectName("pushButton_applyfilter")
        self.horizontalLayout.addWidget(self.pushButton_applyfilter)
        self.pushButton_cleanfilter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cleanfilter.setObjectName("pushButton_cleanfilter")
        self.horizontalLayout.addWidget(self.pushButton_cleanfilter)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setObjectName("pushButton_back")
        self.gridLayout.addWidget(self.pushButton_back, 2, 0, 1, 1)
        self.widget_resultados = QtWidgets.QWidget(self.centralwidget)
        self.widget_resultados.setObjectName("widget_resultados")
        self.gridLayout.addWidget(self.widget_resultados, 1, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Visualización de datos"))
        item = self.tableWidget_reviews.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_reviews.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Etiqueta"))
        item = self.tableWidget_reviews.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre Fichero"))
        item = self.tableWidget_reviews.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sentimiento"))
        item = self.tableWidget_reviews.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Polaridad sentimiento"))
        item = self.tableWidget_reviews.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Subjetividad sentimiento"))
        item = self.tableWidget_reviews.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Valor compound sentimiento"))
        item = self.tableWidget_reviews.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Texto"))
        self.label_filtro.setText(_translate("MainWindow", "Filtro"))
        self.comboBox_filtro.setItemText(0, _translate("MainWindow", "contiene"))
        self.comboBox_filtro.setItemText(1, _translate("MainWindow", "no contiene"))
        self.comboBox_filtro.setItemText(2, _translate("MainWindow", "acaba en"))
        self.comboBox_filtro.setItemText(3, _translate("MainWindow", "no acaba en"))
        self.comboBox_filtro.setItemText(4, _translate("MainWindow", "coinciden minMAYUS"))
        self.comboBox_filtro.setItemText(5, _translate("MainWindow", "coincide exacto"))
        self.comboBox_filtro.setItemText(6, _translate("MainWindow", "empieza por"))
        self.pushButton_applyfilter.setText(_translate("MainWindow", "Aplicar filtro"))
        self.pushButton_cleanfilter.setText(_translate("MainWindow", "Limpiar filtro"))
        self.pushButton_back.setText(_translate("MainWindow", "Atrás"))

