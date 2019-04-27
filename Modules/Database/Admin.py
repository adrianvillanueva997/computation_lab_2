from sqlalchemy.sql import text

from Modules.Database import config as cfg, Encryption


class Admin:
    def __init__(self):
        pass

    @staticmethod
    def get_users_with_projects():
        """
        Funcion que te permite obtener los usuarios con sus proyectos asociados de la base de datos
        :return:
        """
        try:
            with cfg.engine.connect() as con:
                data = {
                    'id_user': [],
                    'email': [],
                    'username': [],
                    'role': [],
                    'id_project': [],
                    'name_project': [],
                    'last_update': [],
                }
                query = 'select * from proyecto_computacion.user usr ' \
                        'join proyecto_computacion.project_rel prj_rel on usr.ID_user = prj_rel.ID_user ' \
                        'join proyecto_computacion.project prj on prj_rel.ID_project = prj.ID_project'
                results = con.execute(query)
                for result in results:
                    data['id_user'].append(result['ID_user'])
                    data['username'].append(result['user_name'])
                    data['email'].append(result['email'])
                    data['role'].append(result['role'])
                    data['name_project'].append(result['name_project'])
                    data['last_update'].append(result['Last_Update'])
            return data
        except Exception as e:
            print(e)

    @staticmethod
    def get_users():
        """Public function that gets all the users in the database

        Returns:
            [dict] -- [dictionary that contains id, username email and role lists.]
        """

        try:
            with cfg.engine.connect() as con:
                query = text('select * from proyecto_computacion.user')
                results = con.execute(query)
                data = {
                    'id': [],
                    'username': [],
                    'email': [],
                    'role': [],
                    'Actividad': []
                }
                for result in results:
                    data['id'].append(str(result['ID_user']))
                    data['username'].append(result['user_name'])
                    data['email'].append(result['email'])
                    data['role'].append(str(result['role']))
                    data['Actividad'].append(str(result['Actividad']))
            return data
        except Exception as e:
            print(e)

    def modificar_usuario(self, id_mo, username, email, role, password):
        """
        Public function that modifies an user params

        Arguments:
            id_mo {[int]} -- [user id]
            username {[string]} -- [username]
            email {[string]} -- [email]
            role {[integer]} -- [role]
            password {[string]} -- [password]
        """
        user = {
            'id': int(id_mo),
            'username': str(username),
            'email': str(email),
            'role': int(role),
            'pass': str(password),
        }
        print(user)
        with cfg.engine.connect() as conn:
            if password is None or password is '':
                query = text('update proyecto_computacion.user '
                             'set user_name=:_username, email=:_email,role=:_role WHERE ID_user like :_id')
                print(query)
                conn.execute(query, _username=user['username'], _email=user['email'], _role=user['role'],
                             _id=user['id'])
            else:
                user['pass'] = Encryption.Encryption.hash_password(password)
                query = text('update proyecto_computacion.user '
                             'set user_name=:_username,email=:_email,role=:_role,password=:_password '
                             'WHERE ID_user like :_id')
                conn.execute(query, _username=user['username'], _email=user['email'], _role=user['role'],
                             _password=user['pass'], _id=user['id'])

    def eliminar_user(self, id):
        """
        Funcion que te permite volver a un usuario activo a inactivo
        :param id:
        :return:
        """
        if id is None:
            raise NotImplementedError()
        try:
            id_user = int(id)
            # TODO
            query = text('update proyecto_computacion.user '
                         'set Actividad=0 '
                         'WHERE ID_user like :_id')
            with cfg.engine.connect() as con:
                con.execute(query, _id=id_user)
        except Exception as e:
            print(e)

    def activar_user(self, id):
        """
        Funcion que permite al administrador activar un usuario
        :param id:
        :return:
        """
        if id is None:
            raise NotImplementedError()
        try:
            id_user = int(id)
            # TODO
            query = text('update proyecto_computacion.user '
                         'set Actividad=1 '
                         'WHERE ID_user like :_id')
            with cfg.engine.connect() as con:
                con.execute(query, _id=id_user)
        except Exception as e:
            print(e)

    def obtener_user(self, id):
        """
        Funcion que te permite todos los datos de un usuario segun su id
        :param id:
        :return:
        """
        try:
            id_user = str(id)
            # TODO
            query = 'SELECT * FROM proyecto_computacion.user WHERE ID_user = ' + id_user
            with cfg.engine.connect() as con:
                results = con.execute(query)
                data = {
                    'id': [],
                    'username': [],
                    'email': [],
                    'role': []
                }
                for result in results:
                    data['id'].append(str(result['ID_user']))
                    data['username'].append(result['user_name'])
                    data['email'].append(result['email'])
                    data['role'].append(str(result['role']))
                print(data)
                return data
        except Exception as e:
            print(e)

    def obtener_id(self, name):
        """
        Funcion que te permite obtener todos los datos de un usuario a partir de su nombre de usuario
        :param name:
        :return:
        """
        try:
            #query = f'SELECT * FROM proyecto_computacion.user where user_name = \"{name}\" LIMIT 1'
            query = text('SELECT * FROM proyecto_computacion.user'
                         ' WHERE user_name = :_nombre LIMIT 1')
            data = {
                'ID_user': [],
                'username': [],
                'email': [],
                'role': []
            }
            with cfg.engine.connect() as con:
                try:

                    results=con.execute(query, _nombre=name)
                    for result in results:
                        data['ID_user'].append(str(result['ID_user']))
                        data['username'].append(result['user_name'])
                        data['email'].append(result['email'])
                        data['role'].append(str(result['role']))
                except Exception as e:
                    data['ID_user'].append(0)
            return data
        except Exception as e:
            print(e)
