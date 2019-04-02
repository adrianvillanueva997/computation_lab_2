from Ventana_superusuario import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
import sys
import ctrl_modificar_usuario
import ctrl_registrar_usuario
import ctr_usuario_proyecto
from Database import config as cfg
from Database import Encryption
import base64
from Database import Admin
from abc import ABC
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
	def __init__(self,*args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.pushButton_Modificar_usuario.clicked.connect(self.modificar_usuario)
		self.pushButton_Registrar_usuario.clicked.connect(self.registrar_usuario)
		self.pushButton_Eliminar_usuario.clicked.connect(self.btn_Eliminar_clicked)
		self.pushButton_Relacion_Proyectos.clicked.connect(self.relacion_proyectos)
		self._main_window = None
	def relacion_proyectos(self):
		self._main_window = ctr_usuario_proyecto.MainWindow()
		self._main_window.load_relacion()
		self._main_window.show()
	def modificar_usuario(self):
		try:
			self._main_window = ctrl_modificar_usuario.MainWindow()
			self._main_window.modificar_lineas(self.tableWidget.selectedItems()[0].text())
			self._main_window.show()
		except Exception as e:
			print(e)
	def registrar_usuario(self):
		self._main_window = ctrl_registrar_usuario.MainWindow()
		self._main_window.show()
	def btn_Eliminar_clicked(self):
		ret=QMessageBox.question(self, 'Advertencia!', "¿Estas seguro de que desea eliminar este usuario?", QMessageBox.Yes | QMessageBox.No )
		if ret == QMessageBox.Yes:
			print('Yes clicked.')
			admin=Admin.Admin()
			try:
				admin.eliminar_user(self.tableWidget.selectedItems()[0].text())
			except Exception as e:
				print(e)
			pass
		else:
			print('No clicked.')
			pass
	def load_usuarios(self):
		try:
			admin=Admin.Admin()
			results = admin.get_users()
			print(results)
			try:
				for i in range(0,len(results['username'])):
					rowPosition = self.tableWidget.rowCount()
					self.tableWidget.insertRow(rowPosition)
					self.tableWidget.setItem(rowPosition,0,QtWidgets.QTableWidgetItem(results['id'][i]))
					self.tableWidget.setItem(rowPosition,1,QtWidgets.QTableWidgetItem(results['username'][i]))
					self.tableWidget.setItem(rowPosition,2,QtWidgets.QTableWidgetItem(results['email'][i]))
					self.tableWidget.setItem(rowPosition,3,QtWidgets.QTableWidgetItem(results['role'][i]))
			except Exception as n:
				print (n)
				print ('cargar datos tabla')
		except Exception as e:
			print(e)
if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.load_usuarios()
	window.show()
	sys.exit(app.exec_())
