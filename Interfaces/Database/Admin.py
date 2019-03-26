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
    @staticmethod
    def modificar_usuario(self, id, username, email, role):
        try:
            user={
                'id': [],
                'username':[],
                'email' : [],
                'role' : [],
            }
            self.user['id'][0]=self.id
            self.user['username'][0]=self.username
            self.user['email'][0]=self.email
            self.user['role'][0]=self.role
            query="UPGRADE proyecto_computacion.user SET user_name='"+ user['username'][0] +"', email='"+user['email'][0]+"', role='"+user['role'][0]+"' WHERE  ID_user='"+user['id'][0]+"'"
            with cfg.engine.connect() as con:
                results = con.execute(query)
                print (results)
        except Exception as e:
            print(e)
