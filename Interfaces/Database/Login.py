# -*- coding: utf-8 -*-
try:
    from Database import config as cfg, Encryption
except Exception as e:
    from Interfaces.Database import config as cfg, Utilities

from sqlalchemy.sql import text


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
                if Encryption.Encryption.verify_password(encrypted_db_password, password):
                    role = result_query[0]['role']
                    id = result_query[0]['ID_user']
                    email = result_query[0]['email']
                    username = result_query['user_name']
                    user_data = {
                        'id': id,
                        'email': email,
                        'username': username,
                        'role': role
                    }
                    return user_data
                else:
                    return None
