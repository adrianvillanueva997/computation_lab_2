from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from Interfaces.Views.Ui_view_clasificar import Ui_MainWindow
from Modules.Database import Project
from Modules.ETL.Classify import Classify


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
        self.pushButton_cleanfilter.clicked.connect(self.clean_filter)
        self.pushButton_guardar_resultados.clicked.connect(self.guardar_resultados)
        self.pushButton_toCSV.clicked.connect(self.export_dataframe_to_csv)
        self._project_id = None
        self._user = None
        self._model_id = None
        self._models = None
        self._dataframe = None
        self._search_models = False

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
        self._search_models = True

    def search_model(self):
        if self._search_models == True:
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
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(item.row(), 2).text()))
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(item.row(), 3).text()))
            self.tableWidget_reviews.setRowHidden(item.row(), True)
        rowCount = self.tableWidget_reviews_to_classify.rowCount()
        if rowCount > 0:
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
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 2).text()))
            self.tableWidget_reviews_to_classify.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 3).text()))
            self.tableWidget_reviews.setRowHidden(i, True)
        self.pushButton_Clasificar.setEnabled(True)
        rowCount = self.tableWidget_reviews_to_classify.rowCount()
        if rowCount > 0:
            self.pushButton_Clasificar.setEnabled(True)

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
        modeloseleccionado = self.comboBox_algoritmo.currentText()
        if modeloseleccionado == "Seleccione un modelo":
            QMessageBox.critical(
                self, "Error", "Hay que especificar un modelo para clasificar")
            return
        rowCount = self.tableWidget_reviews_to_classify.rowCount()
        progreso = self.barra_progreso(rowCount + 20)
        progreso.setValue(0)
        unlabeled_reviews = {
            'reviews': [],
            'labels': []
        }
        for i in range(rowCount):
            progreso.setValue(i)
            unlabeled_reviews['reviews'].append(self.tableWidget_reviews_to_classify.item(i, 4).text())
            unlabeled_reviews['labels'].append(self.tableWidget_reviews_to_classify.item(i, 1).text())
            QtGui.QGuiApplication.processEvents()
        clf = Classify()
        dataframe = clf.classify(unlabeled_reviews, self._project_id, self._model_id)
        progreso.setValue(rowCount + 15)
        QtGui.QGuiApplication.processEvents()
        for i in range(rowCount):
            self.tableWidget_reviews_to_classify.setItem(i, 2, QtWidgets.QTableWidgetItem(dataframe['labels'][i]))
        progreso.setValue(rowCount + 20)
        QtGui.QGuiApplication.processEvents()
        self._dataframe = dataframe
        self.pushButton_guardar_resultados.setEnabled(True)
        self.pushButton_toCSV.setEnabled(True)
        QMessageBox.information(self, "Clasificación completada", "La clasificación se ha completado con éxito")

    def guardar_resultados(self):
        pr = Project.Project(self._user)
        rowCount = self.tableWidget_reviews_to_classify.rowCount()
        progreso = self.barra_progreso(rowCount)
        progreso.setValue(0)
        for i in range(rowCount):
            progreso.setValue(i)
            label = self.tableWidget_reviews_to_classify.item(i, 2).text()
            review_id = self.tableWidget_reviews_to_classify.item(i, 0).text()
            pr.update_review_label(label, review_id)
        self.tableWidget_reviews.setRowCount(0)
        self.load_reviews()
        QMessageBox.information(self, "Cambios guardados", "Los cambios se han guardado con éxito")

    def export_dataframe_to_csv(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Selecciona ruta para guardar los resultados", "",
                                                  "Archivo CSV (*.csv);;All Files (*)", options=options)
        fileName = fileName + ".csv"
        self._dataframe.to_csv(fileName, encoding="utf-8")
        QMessageBox.information(self, "Resultados exportados",
                                "Los resultados se han exportado a un fichero en:\n{}".format(fileName))

    def go_back(self):
        self.close()
        self.parent.show()

    def barra_progreso(self, maximo):
        progress_dialog = QtWidgets.QProgressDialog("Clasificando reviews", "Cancelar", 0, maximo)
        progress_bar = QtWidgets.QProgressBar(progress_dialog)
        progress_dialog.setBar(progress_bar)
        progress_dialog.setWindowModality(QtCore.Qt.WindowModal)
        progress_dialog.setWindowTitle("Clasificando reviews")
        progress_bar.setValue(0)
        progress_bar.setMaximum(maximo)
        progress_dialog.show()

        return progress_dialog
