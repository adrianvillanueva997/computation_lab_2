from PyQt5 import QtWidgets

import Interfaces.Controllers.ctrl_config_project as v_config_project
import Interfaces.Controllers.ctrl_load_files as v_load_files
import Interfaces.Controllers.ctrl_train as v_train
from Interfaces.Views.Ui_view_menu_seleccion import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self._window = None
        self.pushButton_CargarDatos.clicked.connect(self.show_load_files_window)
        self.pushButton_Atras.clicked.connect(self.go_back)
        self.pushButton_Entrenar.clicked.connect(self.show_train_window)
        self.pushButton_ConfiguracionProyecto.clicked.connect(self.show_config_project_window)
        self.parent = None
        self._project_id = None
        self._user = None

    def set_user(self,user):
        self._user = user

    def set_parent(self, MainWindow):
        self.parent = MainWindow

    def go_back(self):
        self.close()
        self.parent.show()

    def show_load_files_window(self):
        self._window = v_load_files.MainWindow()
        self._window.set_parent(self)
        self._window.set_project_id(self._project_id)
        self._window.set_user(self._user)
        self._window.load_labels()
        self._window.show()
        self.close()

    def set_project_id(self, project_id):
        self._project_id = project_id

    def show_train_window(self):
        self._window = v_train.MainWindow()
        self._window.set_parent(self)
        self._window.set_project_id(self._project_id)
        self._window.set_user(self._user)
        self._window.load_reviews()
        self._window.show()
        self.close()

    def show_config_project_window(self):
        self._window = v_config_project.MainWindow()
        self._window.set_parent(self)
        self._window.set_project_id(self._project_id)
        self._window.set_user(self._user)
        self._window.show()
        self.close()
