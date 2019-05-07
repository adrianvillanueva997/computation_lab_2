from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Interfaces.Controllers import ctrl_resultados_entrenamiento as v_resultados
from Interfaces.Views.Ui_view_entrenar import Ui_MainWindow
from Modules.Database import Project
from Modules.ETL import Train


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self._window = None
        self.parent = None
        self.pushButton_back.clicked.connect(self.go_back)
        self.pushButton_add.clicked.connect(self.add_review_to_train)
        self.pushButton_applyfilter.clicked.connect(self.filter_table)
        self.pushButton_remove.clicked.connect(self.remove_from_training_table)
        self.pushButton_Entrenar.clicked.connect(self.train_with_reviews)
        self.pushButton_addall.clicked.connect(self.add_all_reviews)
        self.pushButton_removeall.clicked.connect(self.remove_all_from_training_table)
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

    def add_review_to_train(self):
        rows = self.tableWidget_reviews.selectionModel().selectedRows()
        for item in rows:
            rowPosition = self.tableWidget_reviews_to_train.rowCount()
            self.tableWidget_reviews_to_train.insertRow(rowPosition)
            self.tableWidget_reviews_to_train.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(item.row(), 0).text()))
            self.tableWidget_reviews_to_train.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(item.row(), 1).text()))
            self.tableWidget_reviews_to_train.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(item.row(), 2).text()))
            self.tableWidget_reviews_to_train.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(item.row(), 3).text()))
            self.tableWidget_reviews.setRowHidden(item.row(), True)
        self.pushButton_Entrenar.setEnabled(True)

    def add_all_reviews(self):
        rowCount = self.tableWidget_reviews.rowCount()
        for i in range(0, rowCount):
            rowPosition = self.tableWidget_reviews_to_train.rowCount()
            self.tableWidget_reviews_to_train.insertRow(rowPosition)
            self.tableWidget_reviews_to_train.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 0).text()))
            self.tableWidget_reviews_to_train.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 1).text()))
            self.tableWidget_reviews_to_train.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 2).text()))
            self.tableWidget_reviews_to_train.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(
                self.tableWidget_reviews.item(i, 3).text()))
            self.tableWidget_reviews.setRowHidden(i, True)
        self.pushButton_Entrenar.setEnabled(True)

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

    def remove_from_training_table(self):
        rows = self.tableWidget_reviews_to_train.selectionModel().selectedRows()

        for item in reversed(rows):
            hidden_rows = self.tableWidget_reviews.findItems(
                self.tableWidget_reviews_to_train.item(item.row(), 0).text(), QtCore.Qt.MatchExactly)
            for table_item in hidden_rows:
                self.tableWidget_reviews.setRowHidden(table_item.row(), False)
            self.tableWidget_reviews_to_train.removeRow(item.row())
        rowCount = self.tableWidget_reviews_to_train.rowCount()
        if rowCount < 1:
            self.pushButton_Entrenar.setEnabled(False)

    def remove_all_from_training_table(self):
        rowCount = self.tableWidget_reviews_to_train.rowCount()

        for i in reversed(range(rowCount)):
            hidden_rows = self.tableWidget_reviews.findItems(
                self.tableWidget_reviews_to_train.item(i, 0).text(), QtCore.Qt.MatchExactly)
            for table_item in hidden_rows:
                self.tableWidget_reviews.setRowHidden(table_item.row(), False)
            self.tableWidget_reviews_to_train.removeRow(i)
        self.pushButton_Entrenar.setEnabled(False)

    def train_with_reviews(self):
        reviews_dictionary = {"labels": [], "reviews": []}
        rowCount = self.tableWidget_reviews_to_train.rowCount()
        progreso = self.barra_progreso(rowCount + 20)
        progreso.setValue(0)
        if rowCount < 10:
            QMessageBox.critical(
                self, "Error", "Es necesario un mínimo de 10 reviews para entrenar")
            return
        algoritmo = self.comboBox_algoritmo.currentText()
        if algoritmo == "Selecciona algoritmo":
            QMessageBox.critical(
                self, "Error", "Hay que especificar un algoritmo para el entrenamiento")
            return
        for i in range(0, rowCount):
            progreso.setValue(i)
            QtGui.QGuiApplication.processEvents()
            reviews_dictionary["labels"].append(str(self.tableWidget_reviews_to_train.item(i, 1).text()))
            reviews_dictionary["reviews"].append(str(self.tableWidget_reviews_to_train.item(i, 3).text()))
        train = Train.Train()
        progreso.setValue(rowCount + 10)
        QtGui.QGuiApplication.processEvents()
        modelo = train.trainer(reviews_dictionary, transformer='count_vect', algorithm=str(algoritmo))
        progreso.setValue(rowCount + 20)
        QtGui.QGuiApplication.processEvents()
        QMessageBox.information(self, "Entrenamiento completado", "El entrenamiento se ha completado con éxito")
        self._window = v_resultados.MainWindow()
        self._window.set_project_id(self._project_id)
        self._window.set_model(modelo)
        self._window.set_project_id(self._project_id)
        self._window.set_user(self._user)
        self._window.set_algoritmo(str(algoritmo))
        self._window.cargar_graficos()
        self._window.show()

    def go_back(self):
        self.close()
        self.parent.show()

    def barra_progreso(self, maximo):
        progress_dialog = QtWidgets.QProgressDialog("Entrenando con reviews", "Cancelar", 0, maximo)
        progress_bar = QtWidgets.QProgressBar(progress_dialog)
        progress_dialog.setBar(progress_bar)
        progress_dialog.setWindowModality(QtCore.Qt.WindowModal)
        progress_dialog.setWindowTitle("Entrenando con reviews")
        progress_bar.setValue(0)
        progress_bar.setMaximum(maximo)
        progress_dialog.show()

        return progress_dialog
