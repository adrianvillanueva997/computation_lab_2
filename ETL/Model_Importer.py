import pickle
import tempfile

from Database.Request_Manager import RequestManager


class Model_Importer:
    """
    Public class that exports a model object to a temp file and later reads this object and uploads it to the database
    PATHS:
        * On windows, C:\TEMP, C:\TMP, \TEMP, and \TMP, in the same order.
        * On other platforms, /tmp, /var/tmp, and /usr/tmp, in the same order.
    """

    def __init__(self):
        self.__temp_file = None

    def __export_to_temp_file(self, binary_content):
        tempf = tempfile.NamedTemporaryFile()
        self.__temp_file = tempf
        tempf.close()
        with open(tempf.name, 'wb') as file:
            file.write(binary_content)

    def __read_temp_file_content(self):
        with open(self.__temp_file.name, 'rb') as file:
            model = pickle.load(file)
        return model

    def load_model(self, project_id, model_id):
        request_manager = RequestManager()
        response = request_manager.download_file(project_id, model_id)
        print(response)
        self.__export_to_temp_file(response)
        model = self.__read_temp_file_content()
        print(model)
        return model
