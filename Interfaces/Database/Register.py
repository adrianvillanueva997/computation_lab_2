# -*- coding: utf-8 -*-
try:
    from Interfaces.Database import Encryption, Utilities
    from Interfaces.Database import config as cfg
except Exception as e:
    from Database import Encryption, Utilities
    from Database import config as cfg

from sqlalchemy.sql import text


class Register:
    def __init__(self, username, password, email):
        """
        Class constructor, receives the user username, password and email
        :param username:
        :param password:
        :param email:
        """
        self.__username = username
        self.__password = password
        self.__email = email
        self.__scrape_user_data()

    def __scrape_user_data(self):
        ut = Utilities.Utilities()
        self.__username = ut.scrape_text_for_sql(self.__username)
        self.__email = ut.scrape_text_for_sql(self.__email)
        self.__password = ut.scrape_text_for_sql(self.__password)

    def __check_email(self):
        """
        Checks if the email is already in the database, if it is not in the database, the function will return True
        otherwise, it will return False
        :return:
        """
        with cfg.engine.connect() as con:
            query = text('SELECT * FROM proyecto_computacion.user where email = :_email LIMIT 1')
            results = con.execute(query, _email=self.__email)
            result_query = []
            for result in results:
                result_query.append(result)
            print(len(result_query))
            if len(result_query) is 0:
                return True
            else:
                return False

    def __check_username(self):
        """
        Checks if the username given by the user is in the database, if the username is not in the database, the function will return True,
        otherwise it will return False
        :return:
        """
        with cfg.engine.connect() as con:
            query = text('SELECT * FROM proyecto_computacion.user where user_name = :_username LIMIT 1')
            results = con.execute(query, _username=self.__username)
            result_query = []
            for result in results:
                result_query.append(result)
            print(len(result_query))
            if len(result_query) is 0:
                return True
            else:
                return False

    def upload_user(self):
        """
        Public function that uploads the new user to the database if the email and username are not in the database
        if the register is successful, the function will return True, otherwise, it will return False
        :return:
        """
        if self.__check_email() and self.__check_username():
            with cfg.engine.connect() as con:
                password = Encryption.Encryption.hash_password(self.__password)
                query = text('INSERT INTO proyecto_computacion.user (user_name, email,password)'
                             ' VALUES (:_username,:_email,:_password);')
                con.execute(query, _username=self.__username, _email=self.__email, _password=self.__password)
            return True
        else:
            return False


if __name__ == '__main__':
    re = Register(username='aba', password='1234', email='a')
    re.upload_user()
    re2 = Register(username='bbasa', password='1234', email='b')
    re2.upload_user()
