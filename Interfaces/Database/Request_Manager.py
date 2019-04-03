import requests


class RequestManager:
    def __init__(self):
        pass

    @staticmethod
    def __make_request(user_data):
        """
        Private method that handles and returns the connection with the web server to upload/download files
        :param user_data:
        :return:
        """
        response = requests.post('https://adrianvillanueva.tk/proy_comp2/server.php', user_data)
        response_content = response.content
        return response_content

    def upload_file(self, project_id, user_id, model_id, file_content):
        """
        Public method to upload a file to the web server
        :param project_id:
        :param user_id:
        :param model_id:
        :param file_content:
        :return:
        """
        upload_user_data = {"username": "_api_proy_",
                            "password": "_proy_",
                            "project_id": project_id,
                            "user_id": user_id,
                            "model_id": model_id,
                            "file_content": file_content
                            }
        response = self.__make_request(upload_user_data)
        return response

    def download_file(self, project_id, user_id, model_id):
        """
        Public method to download a file from the server
        :param project_id:
        :param user_id:
        :param model_id:
        :return:
        """
        download_user_data = {"username": "_api_proy_",
                              "password": "_proy_",
                              "project_id": project_id,
                              "user_id": user_id,
                              "model_id": model_id,
                              }
        response = self.__make_request(download_user_data)
        return response


if __name__ == '__main__':
    rm = RequestManager()
    model = (rm.download_file(1, 1, 1))
    print(model)
    # rm.upload_file(1, 2, 5, model)
