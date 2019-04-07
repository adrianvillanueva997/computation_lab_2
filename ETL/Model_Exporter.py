import pickle
import tempfile

from ETL.Modules.Models import Models
from Database.Request_Manager import RequestManager


class Model_Exporter:
    """
    Public class that exports a model object to a temp file and later reads this object and uploads it to the database
    PATHS:
        * On windows, C:\TEMP, C:\TMP, \TEMP, and \TMP, in the same order.
        * On other platforms, /tmp, /var/tmp, and /usr/tmp, in the same order.
    """

    def __init__(self):
        self.__temp_file = None

    def __export_to_temp_file(self, model):
        tempf = tempfile.NamedTemporaryFile()
        self.__temp_file = tempf
        with open(tempf.name, 'wb') as file:
            pickle.dump(model, file)

    def __read_temp_file_content(self):
        with open(self.__temp_file.name, 'rb') as file:
            content = file.read()
        return content

    def export_model(self, model, project_id, model_id):
        self.__export_to_temp_file(model)
        file_content = self.__read_temp_file_content()
        request_manager = RequestManager()
        response = request_manager.upload_file(project_id, model_id, file_content)
        print(response)


if __name__ == '__main__':
    model = Models()
    ml = Model_Exporter()
    ml.export_model(model, 3, 7)
