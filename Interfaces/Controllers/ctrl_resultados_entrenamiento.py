from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox

from Interfaces.Views.Ui_view_resultados_entrenamiento import Ui_MainWindow
from Modules.Database import Project
from Modules.ETL import Model_Exporter
import os

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self._window = None
        self.parent = None
        self._project_id = None
        self._user = None
        self._model = None
        self._algoritmo = None
        self.pushButton_descartar.clicked.connect(self.descartar_modelo)
        self.pushButton_guardarModelo.clicked.connect(self.guardar_modelo)

    def set_user(self,user):
        self._user = user

    def set_project_id(self, project_id):
        self._project_id = project_id

    def set_parent(self, MainWindow):
        self.parent = MainWindow

    def set_model(self,model):
        self._model=model

    def set_algoritmo(self,algoritmo):
        self._algoritmo=algoritmo

    def cargar_graficos(self):
        self._model.generate_classification_model_statistics()
        plt_cfm = self._model.plot_confusion_matrix(self._model.get_labels())

        confusion_matrix = plt_cfm.savefig("matriz_confusion.png")
        pixmap_cfm = QtGui.QPixmap("matriz_confusion.png")
        self.label_matriz_place.setPixmap(pixmap_cfm)
        plt_cv = self._model.plot_sklearn_learning_curve(title="Curva de aprendizaje", X=self._model.get_x_train(),
                                                    y=self._model.get_y_train())
        cross_validation = plt_cv.savefig("cross_validation.png")
        pixmap_cv = QtGui.QPixmap("cross_validation.png")
        self.label_cross_place.setPixmap(pixmap_cv)



    def guardar_modelo(self):
        progreso = self.barra_progreso(5)
        progreso.setValue(0)
        QtGui.QGuiApplication.processEvents()
        pr = Project.Project(self._user)
        nombremodelo=self.lineEdit_nombremodelo.text()
        progreso.setValue(1)
        QtGui.QGuiApplication.processEvents()
        if nombremodelo == "":
            QMessageBox.critical(
                self, "Error", "Hay que especificar un nombre para el modelo")
            return
        model_id = pr.insert_model(self._project_id, nombremodelo, self._algoritmo, "spanish")
        progreso.setValue(2)
        QtGui.QGuiApplication.processEvents()
        exporter = Model_Exporter.Model_Exporter()
        progreso.setValue(3)
        QtGui.QGuiApplication.processEvents()
        exporter.export_model(self._model,self._project_id,model_id)
        progreso.setValue(5)
        QtGui.QGuiApplication.processEvents()
        QMessageBox.information(self, "Modelo guardado", "El modelo se ha guardado con éxito")
        self.close()

    def descartar_modelo(self):
        self._model=None
        os.remove("matriz_confusion.png")
        os.remove("cross_validation.png")
        self.close()

    def barra_progreso(self, maximo):
        progress_dialog = QtWidgets.QProgressDialog("Guardando modelo", "Cancelar", 0, maximo)
        progress_bar = QtWidgets.QProgressBar(progress_dialog)
        progress_dialog.setBar(progress_bar)
        progress_dialog.setWindowModality(QtCore.Qt.WindowModal)
        progress_dialog.setWindowTitle("Guardando modelo")
        progress_bar.setValue(0)
        progress_bar.setMaximum(maximo)
        progress_dialog.show()

        return progress_dialog


