from sqlalchemy.sql import text
try:
    from Database import config as cfg, Encryption
except Exception as e:
    from Interfaces.Database import config as cfg, Utilities


class Admin:
    def __init__(self):
        pass

    @staticmethod
    def get_users_with_projects():
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
                    'role': []
                }
                for result in results:
                    data['id'].append(str(result['ID_user']))
                    data['username'].append(result['user_name'])
                    data['email'].append(result['email'])
                    data['role'].append(str(result['role']))
            return data
        except Exception as e:
            print(e)

    def modificar_usuario(self, id_mo, username, email, role, password):
        """Public function that modifies an user params

        Arguments:
            id_mo {[int]} -- [user id]
            username {[string]} -- [username]
            email {[string]} -- [email]
            role {[integer]} -- [role]
            password {[string]} -- [password]
        """

        user = {
            'id': id_mo,
            'username': username,
            'email': email,
            'role': role,
            'pass': password,
        }
        with cfg.engine.connect() as conn:
            if password is None or password is '':
                query = text(
                    'update proyecto_computacion.user SET (user_name=:_username, email=:_email) WHERE ID_user like :_id')
                conn.execute(
                    query, _username=user['username'], _email=user['email'], _id=user['id'])
            else:
                user['pass'] = Encryption.Encryption.hash_password(password)
                query = text(
                    "update proyecto_computacion.user SET (user_name= :_username, email=:_email, password=:_password) WHERE ID_user like :_id")
                conn.execute(
                    query, _username=user['username'], _email=user['email'], _password=user['password'], _id=user['id'])

    def eliminar_user(self, id):
        if id is None:
            raise NotImplementedError()
        try:
            id_user = str(id)
            # TODO
            query = 'DELETE FROM proyecto_computacion.user WHERE ID_user = ' + id_user
            with cfg.engine.connect() as con:
                results = con.execute(query)
                print(results)
        except Exception as e:
            print(e)

    def obtener_user(self, id):
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
