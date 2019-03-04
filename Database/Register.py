import base64

import config as cfg



class Register:
    def __init__(self, username, password, email):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__con = cfg.engine

    def __check_email(self):
        with self.__con.connect() as con:
            query = f'SELECT * FROM proyecto_computacion.user where email = \"{self.__email}\" LIMIT 1'
            results = con.execute(query)
            result_query = []
            for result in results:
                result_query.append(result)
            print(len(result_query))
            if len(result_query) is 0:
                return True
            else:
                return False

    def __check_username(self):
        with self.__con.connect() as con:
            query = f'SELECT * FROM proyecto_computacion.user where user_name = \"{self.__username}\" LIMIT 1'
            results = con.execute(query)
            result_query = []
            for result in results:
                result_query.append(result)
            print(len(result_query))
            if len(result_query) is 0:
                return True
            else:
                return False

    @staticmethod
    def __encrypt_password(password):
        encrypted_password = (base64.b64encode(bytes(password, encoding='utf-8')))
        return encrypted_password

    def upload_user(self):
        if self.__check_email() and self.__check_username():
            with self.__con.connect() as con:
                password = self.__encrypt_password(self.__password)
                query = f'INSERT INTO proyecto_computacion.user (user_name, email,password)' \
                    f' VALUES (\"{self.__username}\",\"{self.__email}\",\"{password}\");'
                con.execute(query)
            return True
        else:
            return False


if __name__ == '__main__':
    re = Register(username='adrias', password='1234', email='adraas')
    a = re.upload_user()
    print(a)
