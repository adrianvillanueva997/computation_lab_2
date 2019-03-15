from PyQt5 import QtWidgets
from Ui_view_load_files import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def load_files_table(self):
        dic_review = {'label:': [], 'file_name:': [], 'text:': []}
