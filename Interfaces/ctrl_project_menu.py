import ctrl_load_files as v_load_files
from PyQt5 import QtWidgets
from Ui_Menu_seleccion import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self._window = None
        self.pushButton_CargarDatos.clicked.connect(self.show_load_files_window)

    def show_load_files_window(self):
        self._window = v_load_files.MainWindow()
        self._window.show()
