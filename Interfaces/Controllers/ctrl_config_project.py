from PyQt5 import QtWidgets

from Interfaces.Views.Ui_view_config_project import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.parent = None
        self.setupUi(self)
        self._window = None
        self._project_id = None
        self._user = None

    def set_user(self,user):
        self._user = user

    def set_parent(self, MainWindow):
        self.parent = MainWindow

    def set_project_id(self, project_id):
        self._project_id = project_id
