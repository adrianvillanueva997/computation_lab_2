from PyQt5 import QtWidgets

from Modules.Database import Admin
from Interfaces.Views.Ui_view_usuario_proyecto import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,*args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self._main_window = None
    def load_relacion(self):
        admin= Admin.Admin()
        data=admin.get_users_with_projects()
        try:
            for i in range(0,len(data)):
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition,0,QtWidgets.QTableWidgetItem(data['username'][i]))
                self.tableWidget.setItem(rowPosition,1,QtWidgets.QTableWidgetItem(data['name_project'][i]))
        except Exception as e:
            print(e)
        pass