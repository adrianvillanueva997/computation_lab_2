# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clasificar.ui'
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
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.pushButton_Buscar_Ruta = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Buscar_Ruta.setObjectName("pushButton_Buscar_Ruta")
        self.gridLayout_2.addWidget(self.pushButton_Buscar_Ruta, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_Ruta = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Ruta.setObjectName("lineEdit_Ruta")
        self.gridLayout_2.addWidget(self.lineEdit_Ruta, 0, 1, 1, 1)
        self.lineEdit_Nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Nombre.setObjectName("lineEdit_Nombre")
        self.gridLayout_2.addWidget(self.lineEdit_Nombre, 0, 3, 1, 1)
        self.pushButton_Aceptar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Aceptar.setObjectName("pushButton_Aceptar")
        self.gridLayout_2.addWidget(self.pushButton_Aceptar, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.pushButton_Borrar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Borrar.setObjectName("pushButton_Borrar")
        self.gridLayout.addWidget(self.pushButton_Borrar, 4, 1, 1, 1)
        self.pushButton_clasificar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clasificar.setObjectName("pushButton_clasificar")
        self.gridLayout.addWidget(self.pushButton_clasificar, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Etiqueta"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ruta"))
        self.label_2.setText(_translate("MainWindow", "Nombre"))
        self.pushButton_Buscar_Ruta.setText(_translate("MainWindow", "Buscar"))
        self.label.setText(_translate("MainWindow", "Ruta"))
        self.pushButton_Aceptar.setText(_translate("MainWindow", "Aceptar"))
        self.pushButton_Borrar.setText(_translate("MainWindow", "Borrar"))
        self.pushButton_clasificar.setText(_translate("MainWindow", "Clasificar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

