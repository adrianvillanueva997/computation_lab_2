import ctrl_mainwindow as v_main
from Database import Login
from PyQt5 import QtWidgets
from Ui_view_login import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.boton_aceptar.clicked.connect(self.make_login)
        self._main_window = None

    def make_login(self):
        username = self.line_usuario.text()
        password = self.line_password.text()
        lg = Login.Login()
        comprobacion = lg.check_user(username, password)
        if comprobacion == True:
            self._main_window = v_main.MainWindow()
            self._main_window.show()
            self.hide()