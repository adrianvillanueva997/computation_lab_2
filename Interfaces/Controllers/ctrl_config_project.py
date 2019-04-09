from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Interfaces.Views.Ui_view_config_project import Ui_MainWindow
import Interfaces.Controllers.ctrl_gestionar_etiquetas as v_etiquetas
from Database import Project



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.parent = None
        self.setupUi(self)
        self._window = None
        self._project_id = None
        self._user = None
        self.pushButton_Atras.clicked.connect(self.go_back)
        self.pushButton_GestionarEtiquetas.clicked.connect(self.show_labels_window)
        self.pushButton_generarInvitacion.clicked.connect(self.generate_invitation_code)

    def set_user(self,user):
        self._user = user

    def set_parent(self, MainWindow):
        self.parent = MainWindow

    def set_project_id(self, project_id):
        self._project_id = project_id

    def show_labels_window(self):
        self._window = v_etiquetas.MainWindow()
        self._window.set_project_id(self._project_id)
        self._window.set_user(self._user)
        self._window.load_labels()
        self._window.show()

    def generate_invitation_code(self):
        pr = Project.Project(self._user)
        pr.create_invitation_code(self._project_id)
        QMessageBox.information(self, "Código generado", "El código se ha generado con exito")
        self.parent.parent.table_proyectos.setRowCount(0)
        self.parent.parent.load_projects()

    def go_back(self):
        self.parent.show()
        self.close()
