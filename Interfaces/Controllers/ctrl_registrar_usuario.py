from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Interfaces.Views.Ui_view_registrar_usuario import Ui_MainWindow
from Modules.Database import Admin, Register


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.padre = None
        self.pushButton.clicked.connect(self.registrar)
        self.pushButton_Cancelar.clicked.connect(self.cancelar)
        self._main_window = None

    def registrar(self):
        """
        Funcion asociada al boton de registrar. Se encarga de añadir un usuario nuevo a la base de datos, con un rol predefinido de usuario normal
        :return:
        """
        username = self.lineEdit_nombre.text()
        password = self.lineEdit_password.text()
        emilio = self.lineEdit_email.text()
        rg = Register.Register(username, password, emilio)
        registrer_test = rg.upload_user()
        print(registrer_test)
        admin = Admin.Admin()
        if username is None or username == "" or password is None or password == "" or emilio is None or emilio == "":
            QMessageBox.question(self, 'Advertencia!', "ESCRIBA TODOS LOS CAMPOS NECESARIOS EN EL FORMULARIO",
                                 QMessageBox.Ok)
            return
        if registrer_test == True or registrer_test is True:
            ret = QMessageBox.question(self, '¡Advertencia!', "Usuario insertado", QMessageBox.Ok)
            id_us = admin.obtener_id(username)
            print(id_us)
            for i in range(0, len(id_us['ID_user'])):
                id_tem = id_us['ID_user'][i]
                self.padre.add_fila(str(id_tem), username, emilio)
            if ret == QMessageBox.Ok:
                self.close()
        else:
            ret = QMessageBox.question(self, '¡Advertencia!', "Ha ocurrido un error inesperado", QMessageBox.Ok)
            if ret == QMessageBox.Ok:
                self.close()

    def cancelar(self):
        """
        Funcion asociada al boton de cancelar. cierra la ventana automaticamente
        :return:
        """
        self.close()

    def set_parent(self, MainWindow):
        self.padre = MainWindow
