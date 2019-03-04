import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from View_loggin import Ui_MainWindow
import config as cfg
from simplecrypt import encrypt, decrypt
import MySQLdb
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
	def __init__(self,*args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self) 
		self.boton_aceptar.clicked.connect(self.login_addInputTextToListbox)	
	def comprobacion_usuario_pass(usuario, password):
		db = MySQLdb.connect(host="51.15.70.19",user="proy_comp",passwd="teoguapo", db="proyecto_computacion")
		cursor = db.cursor()         # Crear un cursor 
		contr=__encrypt_password(password)
		query = f'SELECT * FROM proyecto_computacion.user where user_name = \"{usuario}\" password=\"{contr}\"'
		results = con.execute(query)
		result_query = []
		for result in results:
			result_query.append(result)
		print(len(result_query))
		if len(result_query) is 0:
			return True
		else:
			return False
		return comprobacion
	def login_addInputTextToListbox(self):
		username=self.line_usuario.text()
		password_usuario=self.line_password.text()
		if username == "":
			QMessageBox.critical(self, "Error","Hay que especificar un usuario")
			return
		if password_usuario == "":
			QMessageBox.critical(self, "Error","Hay que especificar una contraseña")
			return
		db = MySQLdb.connect(host="51.15.70.19",user="proy_comp",passwd="teoguapo", db="proyecto_computacion")
		cursor = db.cursor()         # Crear un cursor 
		contr=encrypt(cfg.encrypton_password, password_usuario)
		query = f'SELECT * FROM user WHERE user_name = \"{username}\" AND passwd = \"{contr}\";'
		print(query)
		#sys.stdout.write(query.decode('utf-8'))
		results = cursor.execute(query)
		result_query = []
		for result in results:
			result_query.append(result)
		print(len(result_query))
		if len(result_query) is 0:
			QMessageBox.critical(self, "Error","Usuario o contraseña erronea")
		else:
			QMessageBox.critical(self, "Correcto","Todo correcto") #aquí enlaca con la pagina proncipal
		comprobar=comprobacion_usuario_pass(username, password_usuario)
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())