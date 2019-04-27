from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Modules.Database import Project
from Interfaces.Views.Ui_view_gestionar_etiquetas import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self._window = None
        self.parent = None
        self._project_id = None
        self._user = None
        self.pushButton_guardar_cambios.clicked.connect(self.guardar_cambios)
        self.pushButton_add.clicked.connect(self.add_label_to_table)
        self.pushButton_cerrar.clicked.connect(self.go_back)
        self.pushButton_eliminar_etiqueta.clicked.connect(self.remove_label_from_table)

    def set_user(self,user):
        self._user = user

    def set_project_id(self, project_id):
        self._project_id = project_id

    def set_parent(self, MainWindow):
        self.parent = MainWindow

    def load_labels(self):
        pr = Project.Project(self._user)
        labels = pr.get_labels(self._project_id)
        for label in labels:
            rowCount = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowCount)
            self.tableWidget.setItem(rowCount,0,QtWidgets.QTableWidgetItem(label))

    def add_label_to_table(self):
        label=self.lineEdit_nuevaetiqueta.text()
        if label == "":
            QMessageBox.critical(
                self, "Error", "El nombre de la etiqueta no puede estar vacío")
            return

        rowCount=self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        self.tableWidget.setItem(rowCount,0,QtWidgets.QTableWidgetItem(label))
        self.tableWidget.resizeColumnsToContents()
        self.lineEdit_nuevaetiqueta.setText("")
        self.pushButton_guardar_cambios.setEnabled(True)

    def remove_label_from_table(self):
        rows = self.tableWidget.selectedItems()
        for item in rows:
            self.tableWidget.removeRow(item.row())
        rowCount = self.tableWidget.rowCount()

        self.pushButton_guardar_cambios.setEnabled(True)

    def guardar_cambios(self):
        pr = Project.Project(self._user)
        pr.remove_labels(self._project_id)
        rowCount = self.tableWidget.rowCount()
        labels = []
        for i in range(rowCount):
            labels.append(self.tableWidget.item(i, 0).text())
        pr.add_labels_to_project(labels, self._project_id)


    def go_back(self):
        self.close()