# -*- coding: utf-8 -*-

from Database import config as cfg, Encryption


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
        self.__con = cfg.engine

    def __check_email(self):
        """
        Checks if the email is already in the database, if it is not in the database, the function will return True
        otherwise, it will return False
        :return:
        """
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
        """
        Checks if the username given by the user is in the database, if the username is not in the database, the function will return True,
        otherwise it will return False
        :return:
        """
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

    def upload_user(self):
        """
        Public function that uploads the new user to the database if the email and username are not in the database
        if the register is successful, the function will return True, otherwise, it will return False
        :return:
        """
        if self.__check_email() and self.__check_username():
            with self.__con.connect() as con:
                password = Encryption.Encryption.hash_password(self.__password)
                query = f'INSERT INTO proyecto_computacion.user (user_name, email,password)' \
                    f' VALUES (\"{self.__username}\",\"{self.__email}\",\"{password}\");'
                con.execute(query)
            return True
        else:
            return False
