from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
import sys
from modificar_usuario import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,*args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton_Aceptar.clicked.connect(self.aceptar)
        self.pushButton_Cancelar.clicked.connect(self.cancelar)
        self._main_window = None
    def datos_usuario(self, nombre):
        self.__name=nombre
    def aceptar(self):
        pass
    def cancelar(self):
        self.close()