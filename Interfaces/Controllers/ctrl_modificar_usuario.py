from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Modules.Database import Admin
from Interfaces.Views.Ui_view_modificar_usuario import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self,*args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton_Aceptar.clicked.connect(self.aceptar)
        self.pushButton_Cancelar.clicked.connect(self.cancelar)
        self.padre=None
        self._main_window = None
    def aceptar(self):
        """
        Esta funcion es la relacionada al boton de aceptar. Inserta los datos en la base de datos y le pasa los datos insertado
        :return:
        """
        admin=Admin.Admin()
        nombre=self.lineEdit_nombre.text()
        passw=self.lineEdit_password.text()
        role=self.lineEdit_Rol.text()
        email=self.lineEdit_email.text()
        if nombre is None or nombre == "" or role is None or role == "" or email is None or email == "":
            QMessageBox.question(self, 'Advertencia!', "ESCRIBA TODOS LOS CAMPOS NECESARIOS EN EL FORMULARIO", QMessageBox.Ok )
            return
        else:
            admin.modificar_usuario(self.id_us , nombre , email , role , passw)
            #self.padre.limpiar_tabla()
            #self.padre.load_usuarios()
            self.padre.modificar_fila(self.id_us,nombre, email, role)
            self.close()
    def cancelar(self):
        """
        Funcion asociada al boton de cancelar
        :return:
        """
        self.close()
    def set_parent(self,MainWindow):
        self.padre = MainWindow
    def modificar_lineas(self , id):
        """
        Funcion que modifica los datos de las diferentes lineas del formulario de modificar
        :param id:
        :return:
        """
        id_usuatio=str(id)
        self.id_us=id_usuatio
        admin= Admin.Admin()
        user=admin.obtener_user(id_usuatio)
        self.lineEdit_nombre.setText(user['username'][0])
        self.role=self.lineEdit_Rol.setText(user['role'][0])
        self.email=self.lineEdit_email.setText(user['email'][0])
