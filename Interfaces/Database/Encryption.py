import binascii
import hashlib
import os


class Encryption:
    def __init__(self):
        pass

    @staticmethod
    def hash_password(password):
        """
        TODO document this according to this website: https://www.vitoshacademy.com/hashing-passwords-in-python/
        :param password:
        :return:
        """
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    @staticmethod
    def verify_password(stored_password, provided_password):
        """
        TODO document this according to this website: https://www.vitoshacademy.com/hashing-passwords-in-python/
        :param stored_password:
        :param provided_password:
        :return:
        """
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password
