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
                #TODO
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

    def modificar_usuario(self, id_mo, username, email, role, password):
        print(id_mo)
        print(type(id_mo))
        print(username)
        print(email)
        print(type(role))
        print(password)
        user={
                'id': [],
                'username':[],
                'email' : [],
                'role' : [],
                'pass' : [],
            }
        user['id'].append(id_mo)
        user['username'].append(username)
        user['email'].append(email)
        user['role'].append(role)
        if password is None:
            #TODO
            query='UPDATE proyecto_computacion.user SET user_name = '+ user['username'][0] +', email = '  +user['email'][0] +" , role = '" +user['role'][0] +"' "+'WHERE  ID_user = '+user['id'][0]
            with cfg.engine.connect() as con:
                con.execute(query)
        print(user)
        if password=='':
            #TODO
            query='UPDATE proyecto_computacion.user SET user_name = '+ user['username'][0] +', email = ' +user['email'][0] +", role = '" +user['role'][0] +"' "+'WHERE  ID_user = '+user['id'][0]+""
            with cfg.engine.connect() as con:
                con.execute(query)
                    #print (results)
        else:
            user['pass'].append(Encryption.Encryption.hash_password(password))
            #TODO
            query="UPDATE proyecto_computacion.user SET user_name="+ user['username'][0] +", email = " +user['email'][0]+" , role = '"+user['role'][0]+"' , password = "+user['pass'][0]+" WHERE  ID_user = "+user['id'][0]
            with cfg.engine.connect() as con:
                con.execute(query)
                    #print (results)

    def eliminar_user(self, id):
        if id is None:
            raise NotImplementedError()
        try:
            id_user= str(id)
            #TODO
            query='DELETE FROM proyecto_computacion.user WHERE ID_user = ' + id_user
            with cfg.engine.connect() as con:
                results = con.execute(query)
                print (results)
        except Exception as e:
            print(e)
    def obtener_user(self, id):
        try:
            id_user= str(id)
            #TODO
            query='SELECT * FROM proyecto_computacion.user WHERE ID_user = ' + id_user
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
                print (data)
                return data
        except Exception as e:
            print(e)