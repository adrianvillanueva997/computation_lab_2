import config as cfg


class Register:
    def __init__(self, username, password, email):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__con = cfg.engine

    def __check_email(self):
        pass

    def __check_user_exists(self):
        with self.__con.connect() as con:
            query = f"SELECT * FROM proyecto_computacion.user where email like {self.__email}"
