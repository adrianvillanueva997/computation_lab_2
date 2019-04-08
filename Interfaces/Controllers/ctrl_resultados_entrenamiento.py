from PyQt5 import QtWidgets, QtGui

from Interfaces.Views.Ui_view_resultados_entrenamiento import Ui_MainWindow
from Database import Project
from ETL import Model_Exporter

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
        pr = Project.Project(self._user)
        nombremodelo=self.lineEdit_nombremodelo.text()
        model_id = pr.insert_model(self._project_id, nombremodelo, self._algoritmo, "spanish")
        exporter = Model_Exporter.Model_Exporter()
        exporter.export_model(self._model,self._project_id,model_id)
        self.close()

    def descartar_modelo(self):
        self._model=None
        self.close()




