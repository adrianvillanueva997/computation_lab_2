from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import Interfaces.Controllers.ctrl_mainwindow as v_main_user
import Interfaces.Controllers.ctrl_ventana_superusuario as v_main_admin
from Database import Login
from Database import User
from Interfaces.Views.Ui_view_login import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.boton_aceptar.clicked.connect(self.make_login)
        self.line_password.returnPressed.connect(self.make_login)
        self._main_window = None

    def make_login(self):
        username = self.line_usuario.text()
        password = self.line_password.text()
        lg = Login.Login()
        user_dict = lg.check_user(username, password)
        print(user_dict)
        if user_dict is None:
            # TODO revisar esto
            QMessageBox.critical(
                self, "Error", "Usuario incorrecto, por favor revise los datos insertados")
            return
        elif user_dict["role"] == 0:
            user = User.User(user_dict["id"])
            self._main_window = v_main_user.MainWindow()
            self._main_window.set_parent(self)
            self._main_window.set_user(user)
            self._main_window.load_projects()
            self._main_window.show()
            self.close()
        elif user_dict["role"] == 1:
            self._main_window = v_main_admin.MainWindow()
            self._main_window.load_usuarios()
            self._main_window.show()
            self.close()
