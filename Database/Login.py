# -*- coding: utf-8 -*-
from sqlalchemy.sql import text

from Database import config as cfg, Encryption, Utilities


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
            ut = Utilities.Utilities()
            user = ut.scrape_text_for_sql(user)
            password = ut.scrape_text_for_sql(password)
            query = text('SELECT * FROM proyecto_computacion.user where user_name = :_user LIMIT 1;')
            results = con.execute(query, _user=user)
            result_query = []
            for result in results:
                result_query.append(result)
            print(len(result_query))
            if len(result_query) is 0:
                return None
            else:
                encrypted_db_password = result_query[0]['password']
                print(encrypted_db_password)
                if Encryption.Encryption.verify_password(encrypted_db_password, password):
                    role = result_query[0]['role']
                    id = result_query[0]['ID_user']
                    email = result_query[0]['email']
                    username = result_query[0]['user_name']
                    user_data = {
                        'id': id,
                        'email': email,
                        'username': username,
                        'role': role
                    }
                    print(user_data)
                    return user_data
                else:
                    return None
