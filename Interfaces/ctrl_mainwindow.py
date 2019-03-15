
from Ui_ventana_principal import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
import ctrl_project_menu as v_project_menu

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton_Seleccionar_Proyecto.clicked.connect(self.show_project_window)
        self._window = None

    def show_project_window(self):
        self._window= v_project_menu.MainWindow()
        self._window.show()
        self.hide()

