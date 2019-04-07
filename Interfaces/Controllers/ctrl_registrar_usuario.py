from Interfaces.Views.Ui_view_registrar_usuario import Ui_MainWindow
from Database import Register, Admin
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
import sys


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,*args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.padre = None
        self.pushButton.clicked.connect(self.registrar)
        self.pushButton_Cancelar.clicked.connect(self.cancelar)
        self._main_window = None
    def registrar(self):
        username = self.lineEdit_nombre.text()
        password = self.lineEdit_password.text()
        emilio=self.lineEdit_email.text()
        rg=Register.Register(username,password,emilio)
        registrer=rg.upload_user()
        admin=Admin.Admin()
        if username is None or username == "" or password is None or password == "" or emilio is None or emilio == "":
            QMessageBox.question(self, 'Advertencia!', "ESCRIBA TODOS LOS CAMPOS NECESARIOS EN EL FORMULARIO",
                                 QMessageBox.Ok)
            return
        if registrer == True:
            ret=QMessageBox.question(self, '¡Advertencia!', "Usuario insertado", QMessageBox.Ok)
            id_us=admin.obtener_id(username)
            self.padre.add_fila(str(id_us['ID_user']), username, emilio, 0,1)
            if ret == QMessageBox.Ok:
                self.close()
        else:
            ret=QMessageBox.question(self, '¡Advertencia!', "Ha ocurrido un error inesperado", QMessageBox.Ok)
            if ret == QMessageBox.Ok:
                self.close()
    def cancelar(self):
        self.close()
    def set_parent(self,MainWindow):
        self.padre = MainWindow
