# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_ventana_superusuario.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
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
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_Eliminar_usuario = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Eliminar_usuario.setObjectName("pushButton_Eliminar_usuario")
        self.gridLayout_2.addWidget(self.pushButton_Eliminar_usuario, 0, 2, 1, 1)
        self.pushButton_Modificar_usuario = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Modificar_usuario.setObjectName("pushButton_Modificar_usuario")
        self.gridLayout_2.addWidget(self.pushButton_Modificar_usuario, 0, 1, 1, 1)
        self.pushButton_Registrar_usuario = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Registrar_usuario.setObjectName("pushButton_Registrar_usuario")
        self.gridLayout_2.addWidget(self.pushButton_Registrar_usuario, 0, 0, 1, 1)
        self.pushButton_Atras = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Atras.setObjectName("pushButton_Atras")
        self.gridLayout_2.addWidget(self.pushButton_Atras, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout_3.addWidget(self.tableWidget, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 2, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.pushButton_Relacion_Proyectos = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Relacion_Proyectos.setObjectName("pushButton_Relacion_Proyectos")
        self.gridLayout.addWidget(self.pushButton_Relacion_Proyectos, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Eliminar_usuario.setText(_translate("MainWindow", "Eliminar/Activar usuario"))
        self.pushButton_Modificar_usuario.setText(_translate("MainWindow", "Modificar usuario"))
        self.pushButton_Registrar_usuario.setText(_translate("MainWindow", "Registrar usuario"))
        self.pushButton_Atras.setText(_translate("MainWindow", "Atras"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Role"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Actividad"))
        self.pushButton_Relacion_Proyectos.setText(_translate("MainWindow", "Relación Proyectos y usuarios"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

