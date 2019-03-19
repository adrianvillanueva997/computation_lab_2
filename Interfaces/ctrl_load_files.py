from PyQt5 import QtWidgets
from Ui_view_load_files import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton_back.clicked.connect(self.go_back)
        self.file_pushButton_add.clicked.connect(self.load_files_table)
        self.parent = None

    def set_parent(self,MainWindow):
        self.parent = MainWindow

    def load_files_table(self):
        label = str(self.comboBox_labels_file.currentText())
        pathFiles = self.file_textEdit_path.text()
        if pathFiles == "":
            QMessageBox.critical(
                self, "Error", "Hay que especificar una ruta antes de añadir un elemento")
            return
        rowPosition = self.file_tableWidget.rowCount()


    def go_back(self):
        self.close()
        self.parent.show()

