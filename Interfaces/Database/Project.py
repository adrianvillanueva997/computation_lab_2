import uuid
from Database import config as cfg
from Database import User


class Project:
    def __init__(self, user):
        """
        Class constructor
        :param user:
        """
        self.__id_user = user.id_user

    def create_project(self, project_name):
        """
        Creates a project and inserts it into the database
        :param project_name:
        :return:
        """
        with cfg.engine.connect() as con:
            insert_project_query = f'INSERT INTO proyecto_computacion.project (name_project) value (\"{project_name}\")'
            select_project_id_query = f'select * from proyecto_computacion.project where name_project = \"{project_name}\"'
            try:
                con.execute(insert_project_query)
                results = con.execute(select_project_id_query)
                id_project = None
                for result in results:
                    id_project = result['ID_project']
                insert_user_relation_query = f'insert into proyecto_computacion.project_rel (id_project, id_user) VALUES ({id_project},{self.__id_user})'
                con.execute(insert_user_relation_query)
            except Exception as e:
                print(e)

    def create_invitation_code(self, id_project):
        """
        Given an id project, generates an invitation uuid64 key to allow other users to take part in 'x' project
        :param id_project:
        :return:
        """
        code = uuid.uuid4()
        code = str(code)
        with cfg.engine.connect() as con:
            try:
                insert_invitation_code_query = f'update proyecto_computacion.project set ID_invitation = \"{code}\" where ID_project = {id_project}'
                con.execute(insert_invitation_code_query)
            except Exception as e:
                print(e)
        return code

    def load_user_projects(self):
        """
        Loads all projects related to the user
        :return:
        """
        with cfg.engine.connect() as con:
            project_data = {
                'id': [],
                'project_name': [],
                'invitation_key': [],
                'timestamp': [],
            }
            try:
                query = f'SELECT * from proyecto_computacion.project prj join proyecto_computacion.project_rel on prj.ID_project = project_rel.ID_project where project_rel.ID_user = {self.__id_user} order by  prj.ID_project asc'
                results = con.execute(query)
                for result in results:
                    print(result)
                    project_data['id'].append(str(result['ID_project']))
                    project_data['project_name'].append(result['name_project'])
                    project_data['timestamp'].append(result['Last_Update'])
                    project_data['invitation_key'].append(result['ID_invitation'])
                    print(project_data)
                return project_data
            except Exception as e:
                print(e)


if __name__ == '__main__':
    user = User(9)
    prj = Project(user)
    prj.create_project("Twitch project")
    data = prj.load_user_projects()
    print(data)
