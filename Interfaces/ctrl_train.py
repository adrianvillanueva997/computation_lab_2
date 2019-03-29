from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from Ui_view_entrenar import Ui_MainWindow
from Database import Project
from Database import User


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
        self._project_id = None

    
    def set_project_id(self,project_id):
        self._project_id=project_id

    def set_parent(self,MainWindow):
        self.parent = MainWindow

    def load_reviews(self):
        user = User.User(10)
        pr = Project.Project(user)
        print(self._project_id)
        reviews = pr.get_project_reviews(self._project_id)
        for i in range(0,len(reviews['file_name'])):
            rowPosition = self.tableWidget_reviews.rowCount()
            self.tableWidget_reviews.insertRow(rowPosition)
            self.tableWidget_reviews.setItem(rowPosition,0,QtWidgets.QTableWidgetItem(reviews['label'][i]))
            self.tableWidget_reviews.setItem(rowPosition,1,QtWidgets.QTableWidgetItem(reviews['file_name'][i]))
            self.tableWidget_reviews.setItem(rowPosition,2,QtWidgets.QTableWidgetItem(reviews['text'][i]))
        self.tableWidget_reviews.resizeColumnsToContents()


    def add_review_to_train(self):
        rows = self.tableWidget_reviews.selectionModel().selectedRows()
        for item in rows:  
            rowPosition = self.tableWidget_reviews_to_train.rowCount()
            self.tableWidget_reviews_to_train.insertRow(rowPosition)
            self.tableWidget_reviews_to_train.setItem(rowPosition,0,QtWidgets.QTableWidgetItem(self.tableWidget_reviews.item(item.row(),0).text()))
            self.tableWidget_reviews_to_train.setItem(rowPosition,1,QtWidgets.QTableWidgetItem(self.tableWidget_reviews.item(item.row(),1).text()))

    def filter_table(self):
        _filter = self.lineEdit_filtro.text()
        items=self.tableWidget_reviews.findItems(_filter,QtCore.Qt.MatchContains)
        print(items)
        for i in range(0,self.tableWidget_reviews.rowCount()):
            self.tableWidget_reviews.setRowHidden(i,True)
        for item in items:
            rowPosition = item.row()
            self.tableWidget_reviews.setRowHidden(rowPosition,False)

        """ items=self.tableWidget_reviews.findItems(_filter,QtCore.Qt.MatchContains)
        print(items)
        for item in items:
            rowPosition = item.row()
            self.tableWidget_reviews.setRowHidden(rowPosition,True) """
    
    def remove_from_training_table(self):
        rows = self.tableWidget_reviews_to_train.selectionModel().selectedRows()

        for item in reversed(rows):
            self.tableWidget_reviews_to_train.removeRow(item.row())
    ##ADRI AQUI TIENES LA FUNCION QUE GENERA EL DICCIONARIO DE REVIEWS CON SUS LABELS
    def train_with_reviews(self):
        reviews_dictionary = {"labels":[], "reviews":[]}
        rowCount = self.tableWidget_reviews_to_train.rowCount()
        for i in range(0,rowCount):  
            reviews_dictionary["labels"].append(self.tableWidget_reviews_to_train.item(i,0).text())
            reviews_dictionary["reviews"].append(self.tableWidget_reviews_to_train.item(i,1).text())
        print (reviews_dictionary)


    def go_back(self):
        self.close()
        self.parent.show()