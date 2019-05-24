from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import Interfaces.Controllers.ctrl_crear_proyecto as v_crear_proyecto
import Interfaces.Controllers.ctrl_project_menu as v_project_menu
from Interfaces.Views.Ui_view_ventana_principal import Ui_MainWindow
from Modules.Database import Project


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.parent = None
        self.setupUi(self)
        self.pushButton_Seleccionar_Proyecto.clicked.connect(self.show_project_window)
        self.pushButton_back.clicked.connect(self.go_back)
        self.pushButton_Crear_proyecto.clicked.connect(self.crear_proyecto)
        self.pushButton_invitation_project.clicked.connect(self.add_project_with_invitation)
        self._window = None
        self._user = None

    def show_project_window(self):
        indexes = self.table_proyectos.selectedIndexes()
        if indexes:
            self._window = v_project_menu.MainWindow()
            self._window.set_parent(self)
            self._window.set_user(self._user)
            for index in sorted(indexes):
                p_id = self.table_proyectos.item(index.row(), 0).text()
                self._window.set_project_id(p_id)
            self._window.show()
            self.close()
        else:
            QMessageBox.critical(
                self, "Error", "Hay que seleccionar un proyecto para continuar")
            return

    def set_parent(self, MainWindow):
        self.parent = MainWindow

    def set_user(self, user):
        self._user = user

    def go_back(self):
        self.close()
        self.parent.show()

    def crear_proyecto(self):
        self._window = v_crear_proyecto.MainWindow()
        self._window.set_parent(self)
        self._window.set_user(self._user)
        self._window.show()

    def load_projects(self):
        pj = Project.Project(self._user)
        projects = pj.load_user_projects()
        for i in range(0, len(projects['id'])):
            rowPosition = self.table_proyectos.rowCount()
            self.table_proyectos.insertRow(rowPosition)
            self.table_proyectos.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(projects['id'][i]))
            self.table_proyectos.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(projects['project_name'][i]))
            self.table_proyectos.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(projects['timestamp'][i])))
            self.table_proyectos.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(projects['invitation_key'][i]))
        self.table_proyectos.resizeColumnsToContents()

    def add_project_with_invitation(self):
        codigoinvitacion, ok = QtWidgets.QInputDialog.getText(self, 'Añadir proyecto con código',
                                                              'Introduce el código de invitación')
        pr = Project.Project(self._user)
        results = pr.add_project_from_invitation(codigoinvitacion)
        if results.rowcount == 0:
            QMessageBox.critical(
                self, "Error", "El código de invitación no pertenece a ningún proyecto")
            return
        self.table_proyectos.setRowCount(0)
        self.load_projects()
