# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Entrenar.ui'
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
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_Etiqueta = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Etiqueta.setObjectName("lineEdit_Etiqueta")
        self.gridLayout_2.addWidget(self.lineEdit_Etiqueta, 2, 1, 1, 1)
        self.lineEdit_Ruta = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Ruta.setObjectName("lineEdit_Ruta")
        self.gridLayout_2.addWidget(self.lineEdit_Ruta, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 2, 1, 1)
        self.pushButton_Buscar_Ruta = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Buscar_Ruta.setObjectName("pushButton_Buscar_Ruta")
        self.gridLayout_2.addWidget(self.pushButton_Buscar_Ruta, 3, 3, 1, 1)
        self.pushButton_Aadir_ruta = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Aadir_ruta.setObjectName("pushButton_Aadir_ruta")
        self.gridLayout_2.addWidget(self.pushButton_Aadir_ruta, 3, 4, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 4, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.pushButton_Entrenar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Entrenar.setObjectName("pushButton_Entrenar")
        self.gridLayout.addWidget(self.pushButton_Entrenar, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Borrar Todo"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Etiqueta"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ruta"))
        self.label.setText(_translate("MainWindow", "Etiqueta"))
        self.label_2.setText(_translate("MainWindow", "Ruta"))
        self.pushButton_Buscar_Ruta.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_Aadir_ruta.setText(_translate("MainWindow", "Añadir"))
        self.pushButton_3.setText(_translate("MainWindow", "Borrar"))
        self.pushButton_Entrenar.setText(_translate("MainWindow", "Entrenar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

