from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from Ui_view_load_files import Ui_MainWindow
from Database.ETL import File_Manager
from Database import File_Uploader
from Interfaces.Web_Scrapping import Amazon_Scrapper
import os



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton_back.clicked.connect(self.go_back)
        self.file_pushButton_add.clicked.connect(self.load_files_table)
        self.file_pushButton_selectfolder.clicked.connect(self.get_folder_path)
        self.file_pushButton_load.clicked.connect(self.load_files_to_db)
        self.file_pushButton_clear.clicked.connect(self.clear_table)
        self.URL_pushButton_add.clicked.connect(self.load_revies_from_url)
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
            print(path)
            file_data,file_names=fm.extract_data_from_files(path)
            fuploader = File_Uploader.File_Uploader(project_id)
            fuploader.upload_reviews_to_db(file_data,file_names)
    
    def clear_table(self):
        self.file_tableWidget.clear()

    def load_revies_from_url(self):
        am_scrap= Amazon_Scrapper.Amazon()
        print(am_scrap)

    def go_back(self):
        self.close()
        self.parent.show()

