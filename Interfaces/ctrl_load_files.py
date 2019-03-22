import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from Database import File_Uploader
from Database.ETL import File_Manager
from Ui_view_load_files import Ui_MainWindow
from Web_Scrapping import Amazon_Scrapper
from Web_Scrapping import Yelp_Scrapper

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton_back.clicked.connect(self.go_back)
        self.file_pushButton_add.clicked.connect(self.load_files_table)
        self.file_pushButton_selectfolder.clicked.connect(self.get_folder_path)
        self.file_pushButton_load.clicked.connect(self.load_files_to_db)
        self.file_pushButton_clear.clicked.connect(self.clear_table)
        self.URL_pushButton_add.clicked.connect(self.load_urls_table)
        self.URL_pushButton_processURLs.clicked.connect(self.load_reviews_urls)
        self.parent = None

    def set_parent(self,MainWindow):
        self.parent = MainWindow

    def load_files_table(self):
        label = str(self.comboBox_labels_file.currentText())
        if label == "Seleccionar etiqueta":
            QMessageBox.critical(
                self, "Error", "Hay que especificar una etiqueta antes de añadir un elemento")
            return
        pathFiles = self.file_lineEditPath.text()
        folderName= os.path.basename(pathFiles)
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
        project_id=self.parent._project_id
        fm = File_Manager.File_Manager()
        numRows = self.file_tableWidget.rowCount()
        for row in range(0,numRows):
            path = str(self.file_tableWidget.item(row,2).text())
            label = str(self.file_tableWidget.item(row,1).text())
            print(path)
            file_data,file_names=fm.extract_data_from_files(path)
            fuploader = File_Uploader.File_Uploader(project_id)
            fuploader.upload_reviews_to_db(file_data,file_names,label)
        
    
    def clear_table(self):
        self.file_tableWidget.setRowCount(0)

    def load_urls_table(self):
        urlPath = self.lineEdit_URL.text()
        if urlPath == "":
            QMessageBox.critical(
                self, "Error", "Hay que especificar una URL")
            return
        rowPosition = self.URL_tableWidget.rowCount()
        self.URL_tableWidget.insertRow(rowPosition)
        self.URL_tableWidget.setItem(
            rowPosition, 0, QtWidgets.QTableWidgetItem(urlPath))
        self.lineEdit_URL.setText("")
        self.URL_pushButton_processURLs.setEnabled(True)

    def load_reviews_urls(self):
        numRows = self.URL_tableWidget.rowCount()
        for row in range(0,numRows):
            url_path = str(self.URL_tableWidget.item(row,0).text())
            if url_path.__contains__('amazon'):
                scrapper = Amazon_Scrapper.Amazon()
                reviews = scrapper.scrape_amazon(url_path)
                print(reviews)
                for item in reviews:
                    rowPosition_reviews=self.URL_review_tableWidget.rowCount()
                    self.URL_review_tableWidget.insertRow(rowPosition_reviews)
                    self.URL_review_tableWidget.setItem(rowPosition_reviews,0,QtWidgets.QTableWidgetItem(url_path))
                    self.URL_review_tableWidget.setItem(rowPosition_reviews,1,QtWidgets.QTableWidgetItem(item))
            if url_path.__contains__('yelp'):
                scrapper = Yelp_Scrapper.Yelp_Scrapper()
                reviews = scrapper.scrapper_yelp(url_path)
                print(reviews)
                for item in reviews:
                    rowPosition_reviews=self.URL_review_tableWidget.rowCount()
                    self.URL_review_tableWidget.insertRow(rowPosition_reviews)
                    self.URL_review_tableWidget.setItem(rowPosition_reviews,0,QtWidgets.QTableWidgetItem(url_path))
                    self.URL_review_tableWidget.setItem(rowPosition_reviews,1,QtWidgets.QTableWidgetItem(item))
        self.URL_tableWidget.setRowCount(0)
        self.URL_pushButton_processURLs.setEnabled(False)




    def go_back(self):
        self.close()
        self.parent.show()
