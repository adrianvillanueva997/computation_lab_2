from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Interfaces.Views.Ui_view_analisis_sentimiento import Ui_MainWindow
from Modules.Database import Project
from Modules.ETL.Modules import Sentiment


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self._window = None
        self.parent = None
        self.pushButton_back.clicked.connect(self.go_back)
        self.pushButton_add.clicked.connect(self.add_review_to_analize)
        self.pushButton_applyfilter.clicked.connect(self.filter_table)
        self.pushButton_remove.clicked.connect(self.remove_from_analize_table)
        self.pushButton_addall.clicked.connect(self.add_all_reviews)
        self.pushButton_removeall.clicked.connect(self.remove_all_from_analize_table)
        self.pushButton_Analizar.clicked.connect(self.analyze_sentiments)
        self.pushButton_guardar_resultados.clicked.connect(self.guardar_resultados)
        self.pushButton_cleanfilter.clicked.connect(self.clean_filter)
        self._project_id = None
        self._user = None

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

    def add_review_to_analize(self):
        rows = self.tableWidget_reviews.selectionModel().selectedRows()
        for item in rows:
            rowPosition = self.tableWidget_reviews_to_analize.rowCount()
            self.tableWidget_reviews_to_analize.insertRow(rowPosition)
            self.tableWidget_reviews_to_analize.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(item.row(), 0).text()))
            self.tableWidget_reviews_to_analize.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(item.row(), 1).text()))
            self.tableWidget_reviews_to_analize.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(item.row(), 2).text()))
            self.tableWidget_reviews_to_analize.setItem(rowPosition, 7, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(item.row(), 3).text()))
            self.tableWidget_reviews.setRowHidden(item.row(), True)
        self.pushButton_Analizar.setEnabled(True)
        self.tableWidget_reviews_to_analize.resizeColumnsToContents()

    def add_all_reviews(self):
        rowCount = self.tableWidget_reviews.rowCount()
        for i in range(0, rowCount):
            rowPosition = self.tableWidget_reviews_to_analize.rowCount()
            self.tableWidget_reviews_to_analize.insertRow(rowPosition)
            self.tableWidget_reviews_to_analize.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 0).text()))
            self.tableWidget_reviews_to_analize.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 1).text()))
            self.tableWidget_reviews_to_analize.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 2).text()))
            self.tableWidget_reviews_to_analize.setItem(rowPosition, 7, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 3).text()))
            self.tableWidget_reviews.setRowHidden(i, True)
        self.pushButton_Analizar.setEnabled(True)
        self.tableWidget_reviews_to_analize.resizeColumnsToContents()

    def filter_table(self):
        _filter = self.lineEdit_filtro.text()
        filtroseleccionado = self.comboBox_filtro.currentText()
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
            self.tableWidget_reviews.setRowHidden(i, False)

    def remove_from_analize_table(self):
        rows = self.tableWidget_reviews_to_analize.selectionModel().selectedRows()

        for item in reversed(rows):
            hidden_rows = self.tableWidget_reviews.findItems(
                self.tableWidget_reviews_to_analize.item(item.row(), 0).text(), QtCore.Qt.MatchExactly)
            for table_item in hidden_rows:
                self.tableWidget_reviews.setRowHidden(table_item.row(), False)
            self.tableWidget_reviews_to_analize.removeRow(item.row())
        rowCount = self.tableWidget_reviews_to_analize.rowCount()
        if rowCount < 1:
            self.pushButton_Analizar.setEnabled(False)
        self.pushButton_guardar_resultados.setEnabled(False)

    def remove_all_from_analize_table(self):
        rowCount = self.tableWidget_reviews_to_analize.rowCount()

        for i in reversed(range(rowCount)):
            hidden_rows = self.tableWidget_reviews.findItems(
                self.tableWidget_reviews_to_analize.item(i, 0).text(), QtCore.Qt.MatchExactly)
            for table_item in hidden_rows:
                self.tableWidget_reviews.setRowHidden(table_item.row(), False)
            self.tableWidget_reviews_to_analize.removeRow(i)
        self.pushButton_Analizar.setEnabled(False)
        self.pushButton_guardar_resultados.setEnabled(False)

    def analyze_sentiments(self):
        analyzer = Sentiment.Sentiment()
        rowCount = self.tableWidget_reviews_to_analize.rowCount()
        progreso = self.barra_progreso(rowCount)
        progreso.setValue(0)
        for i in range(rowCount):
            progreso.setValue(i)
            QtGui.QGuiApplication.processEvents()
            text_to_analyze = self.tableWidget_reviews_to_analize.item(i, 7).text()
            print("TEXTO PARA ANALISIS: {}".format(text_to_analyze))
            sentiments = analyzer.analyse_sentence(str(text_to_analyze))
            sentimiento_predecido = self.pred_sentiment(sentiments)
            self.tableWidget_reviews_to_analize.setItem(i, 3, QtWidgets.QTableWidgetItem(sentimiento_predecido))
            self.tableWidget_reviews_to_analize.setItem(i, 4,
                                                        QtWidgets.QTableWidgetItem(str(sentiments['polarity'][0])))
            self.tableWidget_reviews_to_analize.setItem(i, 5,
                                                        QtWidgets.QTableWidgetItem(str(sentiments['subjectivity'][0])))
            self.tableWidget_reviews_to_analize.setItem(i, 6,
                                                        QtWidgets.QTableWidgetItem(str(sentiments['compound'][0])))
        self.pushButton_guardar_resultados.setEnabled(True)
        QMessageBox.information(self, "Análisis completado", "El análisis se ha completado con éxito")

    def pred_sentiment(self, sentiments):
        polaridad = sentiments['polarity'][0]
        if polaridad > 0.05:
            return "Positivo"
        elif polaridad < -0.05:
            return "Negativo"
        else:
            return "Neutral"

    def guardar_resultados(self):
        rowCount = self.tableWidget_reviews_to_analize.rowCount()
        pr = Project.Project(self._user)
        progreso = self.barra_progreso(rowCount)
        progreso.setValue(0)
        for i in range(rowCount):
            progreso.setValue(i)
            QtGui.QGuiApplication.processEvents()
            id_review = self.tableWidget_reviews_to_analize.item(i, 0).text()
            polaridad = self.tableWidget_reviews_to_analize.item(i, 4).text()
            subjetividad = self.tableWidget_reviews_to_analize.item(i, 5).text()
            compound = self.tableWidget_reviews_to_analize.item(i, 6).text()
            pr.update_sentiments_database(id_review, polaridad, subjetividad, compound)
        QMessageBox.information(self, "Guardado completado", "Los datos se han guardado con éxito")

    def barra_progreso(self, maximo):
        progress_dialog = QtWidgets.QProgressDialog("Realizando análisis de sentimiento", "Cancelar", 0, maximo)
        progress_bar = QtWidgets.QProgressBar(progress_dialog)
        progress_dialog.setBar(progress_bar)
        progress_dialog.setWindowModality(QtCore.Qt.WindowModal)
        progress_dialog.setWindowTitle("Realizando análisis de sentimiento")
        progress_bar.setValue(0)
        progress_bar.setMaximum(maximo)
        progress_dialog.show()
        return progress_dialog

    def go_back(self):
        self.close()
        self.parent.show()
