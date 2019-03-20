from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from Ui_view_entrenar import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self._window = None
        self.parent = None
        self.pushButton_back.clicked.connect(self.go_back)

    
    def set_parent(self,MainWindow):
        self.parent = MainWindow


    def go_back(self):
        self.close()
        self.parent.show()