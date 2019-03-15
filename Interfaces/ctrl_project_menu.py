from Ui_Menu_seleccion import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
import ctrl_load_files as v_load_files
import ctrl_config_project as v_config_project

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self._window = None
        self.pushButton.clicked.connect(self.show_load_files_window)

    def show_load_files_window(self):
        self._window= v_load_files.MainWindow()
        self._window.show()
    
    