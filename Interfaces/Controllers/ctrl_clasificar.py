from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Database import Project
from ETL import Train
from Interfaces.Views.Ui_view_clasificar import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Interfaces.Controllers import ctrl_resultados_entrenamiento as v_resultados

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self._window = None
        self.parent = None
        self.pushButton_back.clicked.connect(self.go_back)
        self.pushButton_add.clicked.connect(self.add_review_to_classify)
        self.pushButton_applyfilter.clicked.connect(self.filter_table)
        self.pushButton_remove.clicked.connect(self.remove_from_classify_table)
        self.pushButton_addall.clicked.connect(self.add_all_reviews)
        self.pushButton_removeall.clicked.connect(self.remove_all_from_classify_table)
        self._project_id = None
        self._user = None

    def set_user(self,user):
        self._user = user

    def set_project_id(self, project_id):
        self._project_id = project_id

    def set_parent(self, MainWindow):
        self.parent = MainWindow

    def load_reviews(self):
        pr = Project.Project(self._user)
        print(self._project_id)
        reviews = pr.get_project_reviews(self._project_id)
        for i in range(0, len(reviews['file_name'])):
            rowPosition = self.tableWidget_reviews.rowCount()
            self.tableWidget_reviews.insertRow(rowPosition)
            self.tableWidget_reviews.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(reviews['id'][i])))
            self.tableWidget_reviews.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(reviews['label'][i]))
            self.tableWidget_reviews.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(reviews['file_name'][i]))
            self.tableWidget_reviews.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(reviews['text'][i]))
        self.tableWidget_reviews.resizeColumnsToContents()

    def add_review_to_classify(self):
        rows = self.tableWidget_reviews.selectionModel().selectedRows()
        for item in rows:
            rowPosition = self.tableWidget_reviews_to_classify.rowCount()
            self.tableWidget_reviews_to_classify.insertRow(rowPosition)
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(item.row(), 0).text()))
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(item.row(), 1).text()))
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(item.row(), 2).text()))
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(item.row(), 3).text()))
            self.tableWidget_reviews.setRowHidden(item.row(), True)
        self.pushButton_Clasificar.setEnabled(True)

    def add_all_reviews(self):
        rowCount = self.tableWidget_reviews.rowCount()
        for i in range(0,rowCount):
            rowPosition = self.tableWidget_reviews_to_classify.rowCount()
            self.tableWidget_reviews_to_classify.insertRow(rowPosition)
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 0).text()))
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 1).text()))
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 2).text()))
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 3).text()))
            self.tableWidget_reviews.setRowHidden(i, True)
        self.pushButton_Clasificar.setEnabled(True)

    def filter_table(self):
        _filter = self.lineEdit_filtro.text()
        items = self.tableWidget_reviews.findItems(_filter, QtCore.Qt.MatchContains)
        print(items)
        for i in range(0, self.tableWidget_reviews.rowCount()):
            self.tableWidget_reviews.setRowHidden(i, True)
        for item in items:
            rowPosition = item.row()
            self.tableWidget_reviews.setRowHidden(rowPosition, False)

        """ items=self.tableWidget_reviews.findItems(_filter,QtCore.Qt.MatchContains)
        print(items)
        for item in items:
            rowPosition = item.row()
            self.tableWidget_reviews.setRowHidden(rowPosition,True) """

    def remove_from_classify_table(self):
        rows = self.tableWidget_reviews_to_classify.selectionModel().selectedRows()

        for item in reversed(rows):
            hidden_rows = self.tableWidget_reviews.findItems(
                self.tableWidget_reviews_to_classify.item(item.row(), 0).text(), QtCore.Qt.MatchExactly)
            for table_item in hidden_rows:
                self.tableWidget_reviews.setRowHidden(table_item.row(), False)
            self.tableWidget_reviews_to_classify.removeRow(item.row())
        rowCount=self.tableWidget_reviews_to_classify.rowCount()
        if rowCount < 1:
            self.pushButton_Clasificar.setEnabled(False)

    def remove_all_from_classify_table(self):
        rowCount = self.tableWidget_reviews_to_classify.rowCount()

        for i in reversed(range(rowCount)):
            hidden_rows = self.tableWidget_reviews.findItems(
                self.tableWidget_reviews_to_classify.item(i, 0).text(), QtCore.Qt.MatchExactly)
            for table_item in hidden_rows:
                self.tableWidget_reviews.setRowHidden(table_item.row(), False)
            self.tableWidget_reviews_to_classify.removeRow(i)
        self.pushButton_Clasificar.setEnabled(False)

    def go_back(self):
        self.close()
        self.parent.show()
