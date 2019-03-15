# -*- coding: utf-8 -*-

from Database import config as cfg
from Database import Encryption


class Login:
    def __init__(self):
        """
        Default class constructor
        """
        pass

    @staticmethod
    def check_user(user, password):
        """
        Public function that checks if the user and password are correct,
        if they are correct, the function will return True
        otherwise it will return False
        :param user:
        :param password:
        :return:
        """
        with cfg.engine.connect() as con:
            query = f'SELECT * FROM proyecto_computacion.user where user_name = \"{user}\" LIMIT 1;'
            results = con.execute(query)
            result_query = []
            for result in results:
                result_query.append(result)
            print(len(result_query))
            if len(result_query) is 0:
                return False
            else:
                encrypted_db_password = result_query[0]['password']

                encrypted_password = self.__encrypt_password(password)
                if str(encrypted_password) == encrypted_db_password:
                    print('coinciden')
                    return True

                if Encryption.Encryption.verify_password(encrypted_db_password, password):
                    return True

