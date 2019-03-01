import config as cfg


class Register:
    def __init__(self, username, password, email):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__con = cfg.engine

    def __check_email(self):
        with self.__con.connect() as con:
            query = f'SELECT * FROM proyecto_computacion.user where email like \"{self.__email}\" LIMIT 1'
            results = con.execute(query)
            query_length = len(results.keys())
            if len(query_length) is not 0:
                return False
            else:
                return True

    def __check_username(self):
        with self.__con.connect() as con:
            query = f'SELECT * FROM proyecto_computacion.user where user_name like \"{self.__username}\" LIMIT 1'
            results = con.execute(query)
            query_length = len(results.keys())
            if len(query_length) is not 0:
                return False
            else:
                return True

    def upload_user(self):
        if (self.__check_email() and self.__check_username()):
            with self.__con.connect() as con:


if __name__ == '__main__':
    re = Register(username='test', password='1234', email='lmao')
    print(re.check_username())
