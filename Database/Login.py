import base64

import config as cfg


class Login:
    def __init__(self):
        pass

    @staticmethod
    def __encrypt_password(password):
        encrypted_password = (base64.b64encode(bytes(password, encoding='utf-8')))
        return encrypted_password

    @staticmethod
    def __dencrypt_password(password):
        password_dencrypted = base64.b64decode(bytes(password, encoding='utf-8'))
        return password_dencrypted

    def comprobacion_usuario_pass(self, usuario, password):
        with cfg.engine.connect() as con:
            query = f'SELECT * FROM proyecto_computacion.user where user_name = \"{usuario}\" LIMIT 1;'
            results = con.execute(query)
            result_query = []
            for result in results:
                result_query.append(result)
            print(len(result_query))
            if len(result_query) is 0:
                return True
            else:
                encrypted_db_password = result_query[0]['password']
                encrypted_password = self.__encrypt_password(password)
                if str(encrypted_password) == encrypted_db_password:
                    print('coinciden')
                    return False


if __name__ == '__main__':
    lg = Login()
    a = lg.comprobacion_usuario_pass(usuario='adrias', password='1234')
    print(a)
