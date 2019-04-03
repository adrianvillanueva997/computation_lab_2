import os
import re

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from Interfaces.Database import File_Manager
from Interfaces.Database import File_Uploader
from Interfaces.Database import Project
from Interfaces.Database import User
from Interfaces.Ui_view_load_files import Ui_MainWindow
from Interfaces.Web_Scrapping import Amazon_Scrapper
from Interfaces.Web_Scrapping import Yelp_Scrapper


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton_back.clicked.connect(self.go_back)
        self.file_pushButton_add.clicked.connect(self.load_files_table)
        self.file_pushButton_selectfolder.clicked.connect(self.get_folder_path)
        self.file_pushButton_load.clicked.connect(self.load_files_to_db)
        self.file_pushButton_clear.clicked.connect(self.file_clear_table)
        self.URL_pushButton_add.clicked.connect(self.load_urls_table)
        self.URL_pushButton_processURLs.clicked.connect(self.load_reviews_urls)
        self.URL_pushButton_clear.clicked.connect(self.url_clear_table_reviews)
        self.URL_pushButton_back.clicked.connect(self.go_back)
        self.URL_pushButton_load.clicked.connect(self.load_reviews_URL_to_db)
        self._project_ID = None
        self.parent = None

    def set_parent(self, MainWindow):
        self.parent = MainWindow

    def load_files_table(self):
        label = str(self.comboBox_labels_file.currentText())
        if label == "Seleccionar etiqueta":
            QMessageBox.critical(
                self, "Error", "Hay que especificar una etiqueta antes de añadir un elemento")
            return
        pathFiles = self.file_lineEditPath.text()
        folderName = os.path.basename(pathFiles)
        if pathFiles == "":
            QMessageBox.critical(
                self, "Error", "Hay que especificar una ruta antes de añadir un elemento")
            return
        rowPosition = self.file_tableWidget.rowCount()
        self.file_tableWidget.insertRow(rowPosition)
        self.file_tableWidget.setItem(
            rowPosition, 0, QtWidgets.QTableWidgetItem(folderName))
        self.file_tableWidget.setItem(
            rowPosition, 1, QtWidgets.QTableWidgetItem(label))
        self.file_tableWidget.setItem(
            rowPosition, 2, QtWidgets.QTableWidgetItem(pathFiles))
        self.file_lineEditPath.setText("")
        self.file_pushButton_load.setEnabled(True)

    def get_folder_path(self):
        file_path = QFileDialog.getExistingDirectory(
            self, 'Selecciona carpeta de ficheros')
        self.file_lineEditPath.setText(file_path)

    def load_files_to_db(self):
        project_id = self._project_ID
        fm = File_Manager.File_Manager()
        numRows = self.file_tableWidget.rowCount()
        for row in range(0, numRows):
            path = str(self.file_tableWidget.item(row, 2).text())
            label = str(self.file_tableWidget.item(row, 1).text())
            print(path)
            file_data, file_names = fm.extract_data_from_files(path)
            fuploader = File_Uploader.File_Uploader(project_id)
            fuploader.upload_reviews_to_db(file_data, file_names, label)

    def file_clear_table(self):
        self.file_tableWidget.setRowCount(0)
        self.file_pushButton_load.setEnabled(False)

    def load_urls_table(self):
        urlPath = self.lineEdit_URL.text()
        if urlPath == "":
            QMessageBox.critical(
                self, "Error", "Hay que especificar una URL")
            return
        if urlPath.__contains__("yelp"):
            print("Contiene")
            print(re.findall(r"https:\/\/www.yelp.es\/biz\/", urlPath))
            if not re.findall(r"https:\/\/www.yelp.es\/biz\/", urlPath):
                QMessageBox.critical(self, "Error", "La URL no tiene el formato correcto")
                return
        elif urlPath.__contains__("amazon"):
            if not re.findall(r"https:\/\/www.amazon.es\/.*\/", urlPath):
                QMessageBox.critical(self, "Error", "La URL no tiene el formato correcto")
                return
        else:
            QMessageBox.critical(
                self, "Error", "URL no soportada")
            return
        rowPosition = self.URL_tableWidget.rowCount()
        self.URL_tableWidget.insertRow(rowPosition)
        self.URL_tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(urlPath))
        self.URL_tableWidget.resizeColumnsToContents()
        self.lineEdit_URL.setText("")
        self.URL_pushButton_processURLs.setEnabled(True)

    def load_reviews_urls(self):
        label = str(self.URL_comboBox_labels.currentText())
        if label == "Seleccionar etiqueta":
            QMessageBox.critical(
                self, "Error", "Hay que especificar una etiqueta antes de añadir un elemento")
            return
        numRows = self.URL_tableWidget.rowCount()
        for row in range(0, numRows):
            url_path = str(self.URL_tableWidget.item(row, 0).text())
            if url_path.__contains__('amazon'):
                scrapper = Amazon_Scrapper.Amazon()
                reviews = scrapper.scrape_amazon(url_path)
                print(reviews)
                for item in reviews:
                    rowPosition_reviews = self.URL_review_tableWidget.rowCount()
                    self.URL_review_tableWidget.insertRow(rowPosition_reviews)
                    self.URL_review_tableWidget.setItem(rowPosition_reviews, 0, QtWidgets.QTableWidgetItem(url_path))
                    self.URL_review_tableWidget.setItem(rowPosition_reviews, 1, QtWidgets.QTableWidgetItem(label))
                    self.URL_review_tableWidget.setItem(rowPosition_reviews, 2, QtWidgets.QTableWidgetItem(item))
                self.URL_review_tableWidget.resizeColumnsToContents()
            if url_path.__contains__('yelp'):
                scrapper = Yelp_Scrapper.Yelp_Scrapper()
                reviews = scrapper.scrapper_yelp(url_path)

                for item in reviews:
                    rowPosition_reviews = self.URL_review_tableWidget.rowCount()
                    self.URL_review_tableWidget.insertRow(rowPosition_reviews)
                    self.URL_review_tableWidget.setItem(rowPosition_reviews, 0, QtWidgets.QTableWidgetItem(url_path))
                    self.URL_review_tableWidget.setItem(rowPosition_reviews, 1, QtWidgets.QTableWidgetItem(label))
                    self.URL_review_tableWidget.setItem(rowPosition_reviews, 2, QtWidgets.QTableWidgetItem(item))
                self.URL_review_tableWidget.resizeColumnsToContents()

        self.URL_tableWidget.setRowCount(0)
        self.URL_pushButton_load.setEnabled(True)
        self.URL_pushButton_processURLs.setEnabled(False)

    def url_clear_table_reviews(self):
        self.URL_review_tableWidget.setRowCount(0)
        self.URL_pushButton_load.setEnabled(False)

    def load_labels(self):
        user = User.User(10)
        pr = Project.Project(user)
        labels = pr.get_labels(self._project_ID)
        self.comboBox_labels_file.clear()
        self.comboBox_labels_file.addItem("Seleccionar etiqueta")
        self.comboBox_labels_file.addItem("Unlabeled")
        self.comboBox_labels_file.addItems(labels)
        self.URL_comboBox_labels.clear()
        self.URL_comboBox_labels.addItem("Seleccionar etiqueta")
        self.URL_comboBox_labels.addItem("Unlabeled")
        self.URL_comboBox_labels.addItems(labels)

    def load_reviews_URL_to_db(self):
        project_id = self._project_ID
        numRows = self.URL_review_tableWidget.rowCount()
        fuploader = File_Uploader.File_Uploader(project_id)
        for row in range(0, numRows):
            name = str(self.URL_review_tableWidget.item(row, 0).text())
            label = str(self.URL_review_tableWidget.item(row, 1).text())
            text = self.URL_review_tableWidget.item(row, 2).text()
            fuploader.upload_single_review_to_db(name, label, text)

    def set_project_id(self, project_id):
        self._project_ID = project_id

    def go_back(self):
        self.close()
        self.parent.show()
