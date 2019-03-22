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
        try:
            with cfg.engine.connect() as con:
                query = 'select * from proyecto_computacion.user'
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
