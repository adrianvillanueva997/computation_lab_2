from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Modules.Database import Project
from Interfaces.Views.Ui_view_visualizacion_datos import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self._window = None
        self.parent = None
        self.pushButton_back.clicked.connect(self.go_back)
        self.pushButton_applyfilter.clicked.connect(self.filter_table)
        self.pushButton_cleanfilter.clicked.connect(self.clean_filter)
        self._project_id = None
        self._user = None
        self._model_id = None
        self._models = None
        self._dataframe = None
        self._search_models=False

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
            sentimiento = self.pred_sentiment(reviews['sentiment_pol'][i])
            self.tableWidget_reviews.setItem(rowPosition,3,QtWidgets.QTableWidgetItem(sentimiento))
            self.tableWidget_reviews.setItem(rowPosition,4,QtWidgets.QTableWidgetItem(str(reviews['sentiment_pol'][i])))
            self.tableWidget_reviews.setItem(rowPosition,5,QtWidgets.QTableWidgetItem(str(reviews['sentiment_sub'][i])))
            self.tableWidget_reviews.setItem(rowPosition,6,QtWidgets.QTableWidgetItem(str(reviews['sentiment_comp'][i])))
            self.tableWidget_reviews.setItem(rowPosition, 7, QtWidgets.QTableWidgetItem(reviews['text'][i]))
        self.tableWidget_reviews.resizeColumnsToContents()


    def filter_table(self):
        _filter = self.lineEdit_filtro.text()
        filtroseleccionado=self.comboBox_filtro.currentText()
        if filtroseleccionado == "contiene":
            items = self.tableWidget_reviews.findItems(_filter, QtCore.Qt.MatchContains)
            for i in range(0, self.tableWidget_reviews.rowCount()):
                self.tableWidget_reviews.setRowHidden(i, True)
            for item in items:
                rowPosition = item.row()
                self.tableWidget_reviews.setRowHidden(rowPosition, False)
        if filtroseleccionado == "no contiene":
            items = self.tableWidget_reviews.findItems(_filter, QtCore.Qt.MatchContains)
            for item in items:
                rowPosition = item.row()
                self.tableWidget_reviews.setRowHidden(rowPosition, True)
        if filtroseleccionado == "acaba en":
            items = self.tableWidget_reviews.findItems(_filter, QtCore.Qt.MatchEndsWith)
            for i in range(0, self.tableWidget_reviews.rowCount()):
                self.tableWidget_reviews.setRowHidden(i, True)
            for item in items:
                rowPosition = item.row()
                self.tableWidget_reviews.setRowHidden(rowPosition, False)
        if filtroseleccionado == "no acaba en":
            items = self.tableWidget_reviews.findItems(_filter, QtCore.Qt.MatchEndsWith)
            for item in items:
                rowPosition = item.row()
                self.tableWidget_reviews.setRowHidden(rowPosition, True)
        if filtroseleccionado == "coinciden minMAYUS":
            items = self.tableWidget_reviews.findItems(_filter, QtCore.Qt.MatchCaseSensitive)
            for i in range(0, self.tableWidget_reviews.rowCount()):
                self.tableWidget_reviews.setRowHidden(i, True)
            for item in items:
                rowPosition = item.row()
                self.tableWidget_reviews.setRowHidden(rowPosition, False)
        if filtroseleccionado == "coincide exacto":
            items = self.tableWidget_reviews.findItems(_filter, QtCore.Qt.MatchExactly)
            for i in range(0, self.tableWidget_reviews.rowCount()):
                self.tableWidget_reviews.setRowHidden(i, True)
            for item in items:
                rowPosition = item.row()
                self.tableWidget_reviews.setRowHidden(rowPosition, False)
        if filtroseleccionado == "empieza por":
            items = self.tableWidget_reviews.findItems(_filter, QtCore.Qt.MatchStartsWith)
            for i in range(0, self.tableWidget_reviews.rowCount()):
                self.tableWidget_reviews.setRowHidden(i, True)
            for item in items:
                rowPosition = item.row()
                self.tableWidget_reviews.setRowHidden(rowPosition, False)

    def clean_filter(self):
        rowCount = self.tableWidget_reviews.rowCount()
        for i in range(rowCount):
            self.tableWidget_reviews.setRowHidden(i,False)


    def go_back(self):
        self.close()
        self.parent.show()

    def pred_sentiment(self,sentimiento):
        if sentimiento:
            print(sentimiento)
            polaridad = float(sentimiento)
            if polaridad > 0.05:
                return "Positivo"
            elif polaridad <-0.05:
                return "Negativo"
            else:
                return "Neutral"
        else:
            return "Sin analizar"