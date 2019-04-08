from PyQt5 import QtWidgets

import Interfaces.Controllers.ctrl_project_menu as v_project_menu
from Database import Project
from Interfaces.Views.Ui_view_ventana_principal import Ui_MainWindow
import Interfaces.Controllers.ctrl_crear_proyecto as v_crear_proyecto


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.parent = None
        self.setupUi(self)
        self.pushButton_Seleccionar_Proyecto.clicked.connect(self.show_project_window)
        self.pushButton_back.clicked.connect(self.go_back)
        self.pushButton_Crear_proyecto.clicked.connect(self.crear_proyecto)
        self._window = None
        self._user = None

    def show_project_window(self):
        self._window = v_project_menu.MainWindow()
        self._window.set_parent(self)
        self._window.set_user(self._user)
        indexes = self.table_proyectos.selectedIndexes()
        for index in sorted(indexes):
            p_id = self.table_proyectos.item(index.row(), 0).text()
            self._window.set_project_id(p_id)
        self._window.show()
        self.close()

    def set_parent(self, MainWindow):
        self.parent = MainWindow

    def set_user(self,user):
        self._user = user

    def go_back(self):
        self.close()
        self.parent.show()

    def crear_proyecto(self):
        self._window=v_crear_proyecto.MainWindow()
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
