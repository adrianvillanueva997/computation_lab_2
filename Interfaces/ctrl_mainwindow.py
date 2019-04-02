

from Ui_view_ventana_principal import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
import ctrl_project_menu as v_project_menu
from Database import Project
from Database import User
from PyQt5 import QtWidgets



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.parent = None
        self.setupUi(self)
        self.pushButton_Seleccionar_Proyecto.clicked.connect(self.show_project_window)
        self.pushButton_back.clicked.connect(self.go_back)
        self._window = None

    def show_project_window(self):
        self._window= v_project_menu.MainWindow()
        self._window.set_parent(self)
        indexes = self.table_proyectos.selectedIndexes()
        for index in sorted(indexes):
            p_id=self.table_proyectos.item(index.row(),0).text()
            self._window.set_project_id(p_id)
        self._window.show()
        self.close()

    def set_parent(self,MainWindow):
        self.parent = MainWindow

    def go_back(self):
        self.close()
        self.parent.show()

    def load_projects(self):
        user = User.User(10)
        pj = Project.Project(user)
        projects = pj.load_user_projects()
        for i in range(0,len(projects)-1):
            rowPosition = self.table_proyectos.rowCount()
            self.table_proyectos.insertRow(rowPosition)
            self.table_proyectos.setItem(rowPosition,0,QtWidgets.QTableWidgetItem(projects['id'][i]))
            self.table_proyectos.setItem(rowPosition,1,QtWidgets.QTableWidgetItem(projects['project_name'][i]))
            self.table_proyectos.setItem(rowPosition,2,QtWidgets.QTableWidgetItem(str(projects['timestamp'][i])))
            self.table_proyectos.setItem(rowPosition,3,QtWidgets.QTableWidgetItem(projects['invitation_key'][i]))
        self.table_proyectos.resizeColumnsToContents()
        


