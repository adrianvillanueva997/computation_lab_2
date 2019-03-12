# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


class MainWindow(QtWidgets.QMainWindow,):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.boton_aceptar.clicked.connect(self.login_addInputTextToListbox)

    def comprobar_usuario(self):
        username = self.line_usuario.text()
        password_usuario = self.line_password.text()
        if username == "":
            QMessageBox.critical(
                self, "Error", "Hay que especificar un usuario")
            return False
        elif password_usuario == "":
            QMessageBox.critical(
                self, "Error", "Hay que especificar una contraseña")
            return False
        else:
            return True

    def login_addInputTextToListbox(self):

        with cfg.engine.connect() as con:
            contr = encrypt(cfg.encrypton_password, password_usuario)
            query = f'SELECT * FROM user WHERE user_name = \"{username}\" AND passwd = \"{contr}\";'
            print(query)
            # sys.stdout.write(query.decode('utf-8'))
            results = cursor.execute(query)
            result_query = []
            for result in results:
                result_query.append(result)
            print(len(result_query))
            if len(result_query) is 0:
                QMessageBox.critical(
                    self, "Error", "Usuario o contraseña erronea")
            else:
                # aquí enlaca con la pagina proncipal
                QMessageBox.critical(self, "Correcto", "Todo correcto")
            comprobar = comprobacion_usuario_pass(username, password_usuario)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
