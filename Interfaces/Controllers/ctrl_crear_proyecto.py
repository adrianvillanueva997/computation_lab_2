from Modules.Database import Project
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Interfaces.Views.Ui_view_crear_proyecto import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.parent = None
        self.setupUi(self)
        self._user = None
        self.pushButton_aceptar.clicked.connect(self.crear_proyecto)
        self.pushButton_cancelar.clicked.connect(self.go_back)
        self.pushButton_addlabel.clicked.connect(self.add_label_to_table)
        self.pushButton_removelabel.clicked.connect(self.remove_label_from_table)

    def set_parent(self, MainWindow):
        self.parent = MainWindow

    def set_user(self,user):
        self._user = user

    def go_back(self):
        self.close()

    def add_label_to_table(self):
        label=self.lineEdit_nuevaEtiqueta.text()
        if label == "":
            QMessageBox.critical(
                self, "Error", "El nombre de la etiqueta no puede estar vacío")
            return

        rowCount=self.tableWidget_etiquetas.rowCount()
        self.tableWidget_etiquetas.insertRow(rowCount)
        self.tableWidget_etiquetas.setItem(rowCount,0,QtWidgets.QTableWidgetItem(label))
        self.tableWidget_etiquetas.resizeColumnsToContents()
        self.lineEdit_nuevaEtiqueta.setText("")
        self.pushButton_aceptar.setEnabled(True)

    def remove_label_from_table(self):
        rows = self.tableWidget_etiquetas.selectedItems()
        for item in rows:
            self.tableWidget_etiquetas.removeRow(item.row())
        rowCount = self.tableWidget_etiquetas.rowCount()

        if rowCount < 1:
            self.pushButton_aceptar.setEnabled(False)
    def crear_proyecto(self):
        pr = Project.Project(self._user)
        nombreproyecto = self.lineEdit_nombreProyecto.text()
        if nombreproyecto == "":
            QMessageBox.critical(
                self, "Error", "Hay que especificar un nombre para el proyecto")
            return

        project_id=pr.create_project(nombreproyecto)
        rowCount = self.tableWidget_etiquetas.rowCount()
        labels=[]
        for i in range(rowCount):
            labels.append(self.tableWidget_etiquetas.item(i,0).text())
        pr.add_labels_to_project(labels,project_id)
        self.parent.table_proyectos.setRowCount(0)
        self.parent.load_projects()
        self.close()