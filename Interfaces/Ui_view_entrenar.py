# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Proyecto Computacion 2\computation-lab-2\Interfaces\view_entrenar.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1044, 626)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget_reviews_to_train = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget_reviews_to_train.setFont(font)
        self.tableWidget_reviews_to_train.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_reviews_to_train.setObjectName("tableWidget_reviews_to_train")
        self.tableWidget_reviews_to_train.setColumnCount(4)
        self.tableWidget_reviews_to_train.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reviews_to_train.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reviews_to_train.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reviews_to_train.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reviews_to_train.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.tableWidget_reviews_to_train, 1, 6, 1, 1)
        self.tableWidget_reviews = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget_reviews.setFont(font)
        self.tableWidget_reviews.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_reviews.setObjectName("tableWidget_reviews")
        self.tableWidget_reviews.setColumnCount(4)
        self.tableWidget_reviews.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reviews.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reviews.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reviews.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reviews.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.tableWidget_reviews, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_filtro = QtWidgets.QLabel(self.centralwidget)
        self.label_filtro.setObjectName("label_filtro")
        self.horizontalLayout.addWidget(self.label_filtro)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.lineEdit_filtro = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_filtro.setObjectName("lineEdit_filtro")
        self.horizontalLayout.addWidget(self.lineEdit_filtro)
        self.pushButton_applyfilter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_applyfilter.setObjectName("pushButton_applyfilter")
        self.horizontalLayout.addWidget(self.pushButton_applyfilter)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout.addWidget(self.pushButton_add)
        self.pushButton_remove = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.verticalLayout.addWidget(self.pushButton_remove)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setObjectName("pushButton_back")
        self.gridLayout.addWidget(self.pushButton_back, 2, 0, 1, 1)
        self.pushButton_Entrenar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Entrenar.setObjectName("pushButton_Entrenar")
        self.gridLayout.addWidget(self.pushButton_Entrenar, 2, 6, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 0, 6, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Entrenamiento"))
        item = self.tableWidget_reviews_to_train.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_reviews_to_train.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Etiqueta"))
        item = self.tableWidget_reviews_to_train.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre Fichero"))
        item = self.tableWidget_reviews_to_train.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Texto"))
        item = self.tableWidget_reviews.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_reviews.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Etiqueta"))
        item = self.tableWidget_reviews.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre Fichero"))
        item = self.tableWidget_reviews.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Texto"))
        self.label_filtro.setText(_translate("MainWindow", "Filtro"))
        self.comboBox.setItemText(0, _translate("MainWindow", "contiene"))
        self.comboBox.setItemText(1, _translate("MainWindow", "no contiene"))
        self.pushButton_applyfilter.setText(_translate("MainWindow", "Aplicar filtro"))
        self.pushButton_add.setText(_translate("MainWindow", "Añadir"))
        self.pushButton_remove.setText(_translate("MainWindow", "Eliminar"))
        self.pushButton_back.setText(_translate("MainWindow", "Atrás"))
        self.pushButton_Entrenar.setText(_translate("MainWindow", "Entrenar"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Selecciona algoritmo"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Naive Bayes"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Decision Tree"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "SVM"))
