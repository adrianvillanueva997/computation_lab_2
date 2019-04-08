from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Database import Project
from ETL.Classify import Classify
from Interfaces.Views.Ui_view_clasificar import Ui_MainWindow


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
        self.comboBox_algoritmo.currentTextChanged.connect(self.search_model)
        self.pushButton_Clasificar.clicked.connect(self.classify_button)
        self._project_id = None
        self._user = None
        self._model_id = None
        self._models = None
        self._dataframe = None

    def set_user(self, user):
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

    def load_models(self):
        pr = Project.Project(self._user)
        print(self._project_id)
        models = pr.get_project_models(self._project_id)
        self.comboBox_algoritmo.clear()
        self.comboBox_algoritmo.addItem("Seleccione un modelo")
        self.comboBox_algoritmo.addItems(models['model_name'])
        self._models = models

    def search_model(self):
        print("hola")
        print(self._models)
        model_name = self.comboBox_algoritmo.currentText()
        found = False
        index = 0
        model_id = 0
        print(model_name)
        while index < len(self._models['model_name']) and found is False:
            print(self._models['model_name'][index])
            if self._models['model_name'][index] == model_name:
                model_id = self._models['id_model'][index]
                found = True
            else:
                index += 1
        self._model_id = model_id

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
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(item.row(), 3).text()))
            self.tableWidget_reviews.setRowHidden(item.row(), True)
        self.pushButton_Clasificar.setEnabled(True)

    def add_all_reviews(self):
        rowCount = self.tableWidget_reviews.rowCount()
        for i in range(0, rowCount):
            rowPosition = self.tableWidget_reviews_to_classify.rowCount()
            self.tableWidget_reviews_to_classify.insertRow(rowPosition)
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 0).text()))
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 1).text()))
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 2).text()))
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(
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

    def remove_from_classify_table(self):
        rows = self.tableWidget_reviews_to_classify.selectionModel().selectedRows()

        for item in reversed(rows):
            hidden_rows = self.tableWidget_reviews.findItems(
                self.tableWidget_reviews_to_classify.item(item.row(), 0).text(), QtCore.Qt.MatchExactly)
            for table_item in hidden_rows:
                self.tableWidget_reviews.setRowHidden(table_item.row(), False)
            self.tableWidget_reviews_to_classify.removeRow(item.row())
        rowCount = self.tableWidget_reviews_to_classify.rowCount()
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

    def classify_button(self):
        rowCount = self.tableWidget_reviews_to_classify.rowCount()
        unlabeled_reviews = {
            'reviews': [],
            'labels': []
        }
        for i in range(rowCount):
            unlabeled_reviews['reviews'].append(self.tableWidget_reviews_to_classify.item(i, 4).text())
            unlabeled_reviews['labels'].append('U')
        clf = Classify()
        dataframe = clf.classify(unlabeled_reviews, self._project_id, self._model_id)
        for i in range(rowCount):
            self.tableWidget_reviews_to_classify.setItem(i, 2, QtWidgets.QTableWidgetItem(dataframe['labels'][i]))
        self._dataframe = dataframe

    def export_dataframe_to_csv(self):
        self._dataframe.to_csv('{RUTA}hola.csv')

    def go_back(self):
        self.close()
        self.parent.show()
