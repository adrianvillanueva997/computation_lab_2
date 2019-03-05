import sys
from Database.Login import Login


if __name__ == "__main__":
    lg = Login()
    a = lg.comprobacion_usuario_pass(usuario='adrias', password='1234')
    print(a)