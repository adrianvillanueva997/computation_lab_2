import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Database import Admin
from Interfaces.Controllers import ctr_usuario_proyecto
from Interfaces.Controllers import ctrl_modificar_usuario
from Interfaces.Controllers import ctrl_registrar_usuario
from Interfaces.Views.Ui_view_ventana_superusuario import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton_Modificar_usuario.clicked.connect(self.modificar_usuario)
        self.pushButton_Registrar_usuario.clicked.connect(self.registrar_usuario)
        self.pushButton_Eliminar_usuario.clicked.connect(self.btn_Eliminar_clicked)
        self.pushButton_Atras.clicked.connect(self.go_back)
        self._main_window = None
        self.parent = None

    def relacion_proyectos(self):
        self._main_window = ctr_usuario_proyecto.MainWindow()
        self._main_window.load_relacion()
        self._main_window.show()

    def go_back(self):
        self.close()
        self.parent.show()

    def modificar_usuario(self):
        try:
            if self.tableWidget.selectedItems()[0].text() is None:
                ret = QMessageBox.question(self, 'Advertencia!',
                                           "TIENE QUE SELECCIONAR EL ID DEL USUARIO QUE DESEA MODIFICAR",
                                           QMessageBox.Ok)
            else:
                self._main_window = ctrl_modificar_usuario.MainWindow()
                self._main_window.modificar_lineas(self.tableWidget.selectedItems()[0].text())
                self._main_window.set_parent(self)
                self._main_window.show()
        except IndexError:
            ret = QMessageBox.question(self, 'Advertencia!',
                                       "TIENE QUE SELECCIONAR EL ID DEL USUARIO QUE DESEA MODIFICAR", QMessageBox.Ok)
        except Exception as e:
            print(e)

    def registrar_usuario(self):
        self._main_window = ctrl_registrar_usuario.MainWindow()
        self._main_window.set_parent(self)
        self._main_window.show()

    def btn_Eliminar_clicked(self):
        ret = QMessageBox.question(self, 'Advertencia!', "¿Estas seguro de que desea eliminar este usuario?",
                                   QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            print('Yes clicked.')
            admin = Admin.Admin()
            try:

                if self.tableWidget.selectedItems()[4].text() == 'Inactivo':
                    try:
                        admin.activar_user(self.tableWidget.selectedItems()[0].text())
                        self.tableWidget.selectedItems()[4].setText('Actvo')
                    except IndexError:
                        ret = QMessageBox.question(self, 'Advertencia!',
                                                   "TIENE QUE SELECCIONAR EL ID DEL USUARIO QUE DESEA MODIFICAR",
                                                   QMessageBox.Ok)
                    except Exception as e:
                        print(e)
                    pass
                else:
                    try:
                        admin.eliminar_user(self.tableWidget.selectedItems()[0].text())
                        self.tableWidget.selectedItems()[4].setText('Inactivo')
                    except IndexError:
                        ret = QMessageBox.question(self, 'Advertencia!',
                                                   "TIENE QUE SELECCIONAR EL ID DEL USUARIO QUE DESEA MODIFICAR",
                                                   QMessageBox.Ok)
                    except Exception as e:
                        print(e)
                    pass
            except IndexError:
                ret = QMessageBox.question(self, 'Advertencia!',
                                           "TIENE QUE SELECCIONAR EL ID DEL USUARIO QUE DESEA MODIFICAR",
                                           QMessageBox.Ok)
            except Exception as e:
                print(e)
        else:
            print('No clicked.')
            pass

    def limpiar_tabla(self):
        self.tableWidget.clearContents()

    def modificar_fila(self, id, nombre, email, role):
        row = self.tableWidget.currentRow()
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(id))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(nombre))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(email))
        if role == str(0):
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem("user"))
        else:
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem("Admin"))

    def add_fila(self, id, nombre, email):
        rowPosition = self.tableWidget.rowCount()
        print('entra en add_fila')
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(id))
        self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(nombre))
        self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(email))
        self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem('user'))
        self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem('Activo'))

    def load_usuarios(self):
        try:
            print("HOLA")
            admin = Admin.Admin()
            results = admin.get_users()
            print(results)
            try:
                for i in range(0, len(results['username'])):
                    rowPosition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)
                    self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(results['id'][i]))
                    self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(results['username'][i]))
                    self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(results['email'][i]))
                    if results['role'][i] == str(0):
                        self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem('user'))
                    else:
                        self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem('admin'))
                    # self.tableWidget.setItem(rowPosition,3,QtWidgets.QTableWidgetItem(results['role'][i]))
                    if results['Actividad'][i] == str(0):
                        self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem('Inactivo'))
                    else:
                        self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem('Activo'))
                data2 = admin.get_users_with_projects()
                print(data2)
                try:
                    for i in range(0, len(data2)):
                        rowPosition2 = self.tableWidget.rowCount()
                        self.tableWidget_Poryectos.insertRow(rowPosition2)
                        self.tableWidget_Poryectos.setItem(rowPosition2, 0, QtWidgets.QTableWidgetItem(data2['username'][i]))
                        self.tableWidget_Poryectos.setItem(rowPosition2, 1, QtWidgets.QTableWidgetItem(data2['name_project'][i]))
                except Exception as np :
                    print(np)
            except Exception as n:
                print(n)
                print('cargar datos tabla')
        except Exception as e:
            print(e)

    def set_parent(self, MainWindow):
        self.parent = MainWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.load_usuarios()
    window.show()
    sys.exit(app.exec_())
