from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
import sys
from modificar_usuario import Ui_MainWindow
try:
    from Interfaces.Database import config as cfg, Encryption, Admin
except Exception as e:
    from Database import config as cfg, Utilities, Admin

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self,*args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton_Aceptar.clicked.connect(self.aceptar)
        self.pushButton_Cancelar.clicked.connect(self.cancelar)
        self.padre=None
        self._main_window = None
    def aceptar(self):
        admin=Admin.Admin()
        nombre=self.lineEdit_nombre.text()
        passw=self.lineEdit_password.text()
        role=self.lineEdit_Rol.text()
        email=self.lineEdit_email.text()
        if nombre is None or nombre == '' or role is None or role == ''or email is None or email == '' :
            QMessageBox.question(self, 'Advertencia!', "ESCRIBA TODOS LOS CAMPOS NECESARIOS EN EL FORMULARIO", QMessageBox.Ok )
            pass
        else:
            admin.modificar_usuario(self.id_us , nombre , email , role , passw)
            #self.padre.limpiar_tabla()
            #self.padre.load_usuarios()
            self.padre.modificar_fila(self.id_us,nombre, email, role)
            self.close()
    def cancelar(self):
        self.close()
    def set_parent(self,MainWindow):
        self.padre = MainWindow
    def modificar_lineas(self , id):
        id_usuatio=str(id)
        self.id_us=id_usuatio
        admin=Admin.Admin()
        user=admin.obtener_user(id_usuatio)
        self.lineEdit_nombre.setText(user['username'][0])
        self.role=self.lineEdit_Rol.setText(user['role'][0])
        self.email=self.lineEdit_email.setText(user['email'][0])
