import uuid

from sqlalchemy.sql import text

from Database import User, Utilities
from Database import config as cfg
from ETL.Modules import Sentiment


class Project:
    def __init__(self, user):
        """
        Class constructor
        :param user:
        """
        self.__id_user = user.id_user
        self.failed_reviews_sentiment = []
        self.failed_reviews_label = []

    def create_project(self, project_name):
        """
        Creates a project and inserts it into the database
        :param project_name:
        :return:
        """
        with cfg.engine.connect() as con:
            insert_project_query = text(
                'INSERT INTO proyecto_computacion.project (name_project,Last_Update) '
                'value (:_project_name, CURRENT_TIMESTAMP)')
            select_project_id_query = text('select * from proyecto_computacion.project prj'
                                           ' where prj.name_project = :_project_name'
                                           ' order by prj.Last_Update ASC limit 1')
            try:
                insert = con.execute(insert_project_query, _project_name=project_name)
                pr_id = insert.lastrowid
                results = con.execute(select_project_id_query, _project_name=project_name)
                id_project = None
                for result in results:
                    id_project = result['ID_project']
                insert_user_relation_query = text('insert into proyecto_computacion.project_rel '
                                                  '(id_project, id_user) VALUES (:_id_project,:_id_user)')
                con.execute(insert_user_relation_query, _id_project=id_project, _id_user=self.__id_user)
                return pr_id
            except Exception as e:
                print(e)

    @staticmethod
    def create_invitation_code(id_project):
        """
        Given an id project, generates an invitation uuid64 key to allow other users to take part in 'x' project
        :param id_project:
        :return:
        """
        code = uuid.uuid4()
        code = str(code)
        with cfg.engine.connect() as con:
            try:
                insert_invitation_code_query = text('update proyecto_computacion.project '
                                                    'set ID_invitation = :_invitation_code '
                                                    'where ID_project = :_project_id')
                con.execute(insert_invitation_code_query, _invitation_code=code, _project_id=id_project)
            except Exception as e:
                print(e)
        return code


    def add_project_from_invitation(self,invitation_code):
        with cfg.engine.connect() as con:
            try:
                query = text('SELECT * FROM proyecto_computacion.project where ID_invitation = :_invitation_code')
                results=con.execute(query,_invitation_code=invitation_code)

                id_project = None
                for result in results:
                    id_project = result['ID_project']
                print("hola")
                print(id_project)
                if id_project is not None:
                    print("entra")
                    insert_user_relation_query = text('insert into proyecto_computacion.project_rel '
                                                      '(id_project, id_user) VALUES (:_id_project,:_id_user)')
                    con.execute(insert_user_relation_query, _id_project=id_project, _id_user=self.__id_user)
                    return results

                return results
            except Exception as e:
                print(e)


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
                query = text('SELECT * from proyecto_computacion.project prj join'
                             ' proyecto_computacion.project_rel on prj.ID_project = project_rel.ID_project '
                             'where project_rel.ID_user = :_user_id order by  prj.ID_project asc')
                results = con.execute(query, _user_id=self.__id_user)
                for result in results:
                    project_data['id'].append(str(result['ID_project']))
                    project_data['project_name'].append(result['name_project'])
                    project_data['timestamp'].append(result['Last_Update'])
                    project_data['invitation_key'].append(result['ID_invitation'])
                return project_data
            except Exception as e:
                print(e)

    @staticmethod
    def get_project_reviews(project_id):
        data = {
            'id': [],
            'label': [],
            'file_name': [],
            'text': [],
            'sentiment_pol': [],
            'sentiment_sub': [],
            'sentiment_comp': []
        }
        try:
            with cfg.engine.connect() as con:

                query = text('SELECT * from proyecto_computacion.project prj join proyecto_computacion.review '
                             'on prj.ID_project = review.ID_project where prj.ID_project like :_project_id')
                results = con.execute(query, _project_id=project_id)
                for result in results:
                    data['id'].append(result['ID_review'])
                    data['label'].append(result['label'])
                    data['file_name'].append(result['file_name'])
                    data['text'].append(result['text_review'])
                    data['sentiment_pol'].append(result['sentiment_pol'])
                    data['sentiment_sub'].append(result['sentiment_sub'])
                    data['sentiment_comp'].append(result['sentiment_comp'])
            return data
        except Exception as e:
            print(e)

    def update_sentiments_database(self,review_id,polarity,subjectivity,compound):

        try:
            with cfg.engine.connect() as con:
                query = text('UPDATE proyecto_computacion.review SET sentiment_pol =:_sentiment_pol, '
                             'sentiment_sub=:_sentiment_sub,sentiment_comp=:_sentiment_comp WHERE ID_review=:_review_id')
                con.execute(query, _sentiment_pol=float(polarity), _sentiment_sub=float(subjectivity),
                            _sentiment_comp=float(compound), _review_id=float(review_id))

        except Exception as e:
            print(e)


    def update_review_label(self,label,id):

        try:
            with cfg.engine.connect() as con:
                query = text('UPDATE proyecto_computacion.review SET label=:_label WHERE ID_review=:_review_id')
                con.execute(query, _label=str(label),_review_id=int(id))

        except Exception as e:
            print(e)


    def update_sentiments(self, project_id):
        """
        Given a project id, do sentiment analysis on those reviews that haven't been analysed yet.
        This method will update their compound, polarity and subjectivity.
        :param project_id:
        :return:
        """
        try:
            failed_reviews = []
            with cfg.engine.connect() as con:
                sentiment = Sentiment.Sentiment()
                query = text('SELECT * FROM proyecto_computacion.project prj join proyecto_computacion.review '
                             'on prj.ID_project = review.ID_project '
                             'where prj.ID_project like :_project_id and sentiment_pol is null')
                results = con.execute(query, _project_id=project_id)
                for result in results:
                    try:
                        review_id = result['ID_review']
                        text = result['text_review']
                        sentiments = sentiment.analyse_sentence(text)
                        update_query = text("update proyecto_computacion.review set "
                                            "sentiment_pol = :_polarity,"  # sentiments['polarity'][0]v
                                            "sentiment_sub = :_subjectivity,"
                                            "sentiment_comp = :_compound "
                                            "where ID_review like :_id_review")
                        con.execute(update_query, _polarity=sentiments['polarity'][0],
                                    _subjectivity=sentiments['subjectivity'][0],
                                    _compound=sentiments['compound'][0], _id_review=review_id)

                    except Exception as e:
                        print(e)
                        failed_reviews.append(text)
                        self.failed_reviews = failed_reviews
        except Exception as e:
            print(e)

    def classify_reviews(self, model, project_id):
        # TODO
        pass

    @staticmethod
    def add_labels_to_project(labels, project_id):
        """
        Public method that adds labels to a project
        :param labels:
        :param project_id:
        :return:
        """
        try:
            with cfg.engine.connect() as con:
                for label in labels:
                    try:
                        ut = Utilities.Utilities()
                        label = ut.scrape_text_for_sql(label)
                        query = text('insert into proyecto_computacion.Label'
                                     ' (label_text, ID_Project) VALUES (:_label_text,:_project_id);')
                        print(query)
                        con.execute(query, _label_text=label, _project_id=project_id)
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)

    @staticmethod
    def add_urls_to_project(project_id, urls):
        """
        Public method that adds urls to a project (by default they are unprocessed aka 0)
        :param project_id:
        :param urls:
        :return:
        """
        try:
            with cfg.engine.connect() as con:
                for url in urls:
                    try:
                        ut = Utilities.Utilities()
                        url = ut.scrape_text_for_sql(url)
                        query = text('INSERT INTO proyecto_computacion.link_web_scrapper (ID_project, url, processed) '
                                     'values (:_project_id,:_url,0)')
                        con.execute(query, _project_id=project_id, _url=url)
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)

    @staticmethod
    def get_labels(project_id):
        """
        Public method that gets the labels associated to a project
        :param project_id:
        :return:
        """
        try:
            with cfg.engine.connect() as con:
                query = text('SELECT * FROM proyecto_computacion.Label where ID_Project like :_project_id')
                results = con.execute(query, _project_id=project_id)
                labels = []
                for result in results:
                    labels.append(result['label_text'])
            return labels
        except Exception as e:
            print(e)

    @staticmethod
    def remove_labels(project_id):
        try:
            with cfg.engine.connect() as con:
                query = text('DELETE FROM proyecto_computacion.Label where ID_Project like :_project_id')
                results = con.execute(query, _project_id=project_id)
            return results
        except Exception as e:
            print(e)

    @staticmethod
    def check_urls(urls):
        """
        Public method to check if a url is good or bad.
        Returns a tuple with 2 lists, one with good urls and one with bad urls
        :param urls:
        :return:
        """
        valid_urls = []
        not_valid_urls = []
        for url in urls:
            if str(url).__contains__('amazon') or str(url).__contains__('metacritic'):
                valid_urls.append(url)
            else:
                not_valid_urls.append(url)
        return valid_urls, not_valid_urls

    @staticmethod
    def get_reviews_by_label(label, project_id):
        """
        Public method that returns all the reviews with 'X' label
        :param label:
        :param project_id:
        :return:
        """
        try:
            with cfg.engine.connect() as con:
                query = text('SELECT * FROM proyecto_computacion.review '
                             'where label like :_label and  ID_project like :_project_id')
                results = con.execute(query, _label=label, _project_id=project_id)
                query_result = {
                    'id': [],
                    'label': [],
                    'file_name': [],
                    'text_review': [],
                    'sentiment_pol': [],
                    'sentiment_sub': [],
                    'sentiment_comp': []
                }
                for result in results:
                    query_result['id'].append(result['ID_review'])
                    query_result['label'].append(result['label'])
                    query_result['file_name'].append(result['file_name'])
                    query_result['text_review'].append(result['text_review'])
                    query_result['sentiment_pol'].append(result['sentiment_pol'])
                    query_result['sentiment_sub'].append(result['sentiment_sub'])
                    query_result['sentiment_comp'].append(result['sentiment_comp'])
            return query_result
        except Exception as e:
            print(e)

    @staticmethod
    def get_urls_not_processed(project_id):
        """
        Public method that returns the urls that have not been processed
        :param project_id:
        :return:
        """
        try:
            with cfg.engine.connect() as con:
                query = text(
                    'select * from proyecto_computacion.link_web_scrapper '
                    'where processed like 0 and ID_project like :_project_id')
                results = con.execute(query, _project_id=project_id)
                urls = []
                for result in results:
                    urls.append(result['url'])
            return urls
        except Exception as e:
            print(e)

    @staticmethod
    def get_processed_urls(project_id):
        """
        Public method that returns the urls that have been processed
        :param project_id:
        :return:
        """
        try:
            with cfg.engine.connect() as con:
                query = text('select * from proyecto_computacion.link_web_scrapper '
                             'where processed like 1 and ID_project like :_project_id')
                results = con.execute(query, _project_id=project_id)
                urls = []
                for result in results:
                    urls.append(result['url'])
            return urls
        except Exception as e:
            print(e)

    @staticmethod
    def update_url_status(url, project_id):
        """
        public method that updates the status of certain url
        :param url:
        :param project_id:
        :return:
        """
        try:
            with cfg.engine.connect() as con:
                query = text('UPDATE proyecto_computacion.link_web_scrapper set'
                             ' processed= 1 where url like :_url and ID_project like :_project_id')
                con.execute(query, _url=url, _project_id=project_id)
        except Exception as e:
            print(e)

    @staticmethod
    def get_url_id(url, project_id):
        """
        Public method that receives a project id and a url and retrieves the url ID
        :param url:
        :param project_id:
        :return:
        """
        try:
            with cfg.engine.connect() as con:
                query = text('SELECT * from proyecto_computacion.link_web_scrapper'
                             ' where url like :_url and ID_project like :_project_id')
                results = con.execute(query, _url=url, _project_id=project_id)
                id = ''
                for result in results:
                    id = result['ID_link']
            return id
        except Exception as e:
            print(e)

    def upload_scrapped_review(self, project_id, reviews, url):
        # TODO
        pass

    @staticmethod
    def get_project_models(project_id):
        """
        Public method that returns all the models related with a model given a project id
        :param project_id:
        :return:
        """
        try:
            with cfg.engine.connect() as con:
                query = text('SELECT * from proyecto_computacion.model where ID_project like :_project_id')
                results = con.execute(query, _project_id=project_id)
                results_dict = {
                    'id_model': [],
                    'id_project': [],
                    'model_name': [],
                    'algorithm': [],
                    'language': [],
                    'accuracy': []
                }
                for result in results:
                    results_dict['id_model'].append(str(result['ID_model']))
                    results_dict['id_project'].append(str(result['ID_project']))
                    results_dict['model_name'].append(result['model_name'])
                    results_dict['algorithm'].append(result['algorithm'])
                    results_dict['language'].append(result['language'])

            return results_dict
        except Exception as exception:
            print(exception)

    @staticmethod
    def get_project_models_by_language(project_id, language):
        """
        Public method that returns all models by language given a project id and a language
        :param project_id:
        :param language:
        :return:
        """
        try:
            with cfg.engine.connect() as con:
                query = text(
                    'SELECT * from proyecto_computacion.model '
                    'where ID_project like :_project_id and language like :_language')
                results = con.execute(query, _project_id=project_id, _language=language)
                results_dict = {
                    'id_model': [],
                    'id_project': [],
                    'model_name': [],
                    'algorithm': [],
                    'language': [],
                    'accuracy': []
                }
                for result in results:
                    results_dict['id_model'].append(str(result['ID_model']))
                    results_dict['id_project'].append(str(result['ID_project']))
                    results_dict['model_name'].append(result['model_name'])
                    results_dict['algorithm'].append(result['algorithm'])
                    results_dict['language'].append(result['language'])

            return results_dict
        except Exception as exception:
            print(exception)

    @staticmethod
    def get_project_models_by_algorithm(project_id, algorithm):
        """
        Public method that returns all models from a project given a project id and an algorithm
        :param project_id:
        :param algorithm:
        :return:
        """
        try:
            with cfg.engine.connect() as con:
                query = text('SELECT * from proyecto_computacion.model '
                             'where ID_project like :_project_id and algorithm like :_algorithm')
                results = con.execute(query, _project_id=project_id, _algorithm=algorithm)
                results_dict = {
                    'id_model': [],
                    'id_project': [],
                    'model_name': [],
                    'algorithm': [],
                    'language': [],
                    'accuracy': []
                }
                for result in results:
                    results_dict['id_model'].append(str(result['ID_model']))
                    results_dict['id_project'].append(str(result['ID_project']))
                    results_dict['model_name'].append(result['model_name'])
                    results_dict['algorithm'].append(result['algorithm'])
                    results_dict['language'].append(result['language'])

            return results_dict
        except Exception as exception:
            print(exception)

    @staticmethod
    def get_models_by_language_and_algorithm(project_id, algorithm, language):
        """
        Public function that returns all the models from a project given a certain algorithm and a language
        :param project_id:
        :param algorithm:
        :param language:
        :return:
        """
        try:
            with cfg.engine.connect() as con:
                query = text('SELECT * from proyecto_computacion.model '
                             'where ID_project like :_project_id and algorithm '
                             'like :_algorithm and language like :_language')
                results = con.execute(query, _project_id=project_id, _algorithm=algorithm, _language=language)
                results_dict = {
                    'id_model': [],
                    'id_project': [],
                    'model_name': [],
                    'algorithm': [],
                    'language': [],
                    'accuracy': []
                }
                for result in results:
                    results_dict['id_model'].append(str(result['ID_model']))
                    results_dict['id_project'].append(str(result['ID_project']))
                    results_dict['model_name'].append(result['model_name'])
                    results_dict['algorithm'].append(result['algorithm'])
                    results_dict['language'].append(result['language'])

            return results_dict
        except Exception as exception:
            print(exception)

    @staticmethod
    def insert_model(id_project, model_name, algorithm, language):
        """
        Public method that inserts a model given a project id, model name, algorithm and language
        :param id_project:
        :param model_name:
        :param algorithm:
        :param language:
        :return:
        """
        try:
            with cfg.engine.connect() as con:
                query = text('INSERT INTO proyecto_computacion.model (ID_project, model_name, language, algorithm)'
                             f'VALUES (:_id_project,:_model_name,:_language,:_algorithm)')
                results = con.execute(query, _id_project=id_project, _model_name=model_name,
                                      _algorithm=algorithm, _language=language)
                return results.lastrowid
        except Exception as e:
            print(e)


if __name__ == '__main__':
    user = User.User(10)
    prj = Project(user)
    labels = ['a', 'b', 'c', 'd']
    urls = ['https://www.amazon.es/New-Super-Mario-Bros-Deluxe/dp/B07HD1312V/',
            'https://www.amazon.es/Donkey-Kong-Country-Tropical-Freeze/dp/B078YJ7TLT/',
            'https://www.metacritic.com/game/pc/dota-2/', 'https://pornhub.com']

    valid_urls, not_valid_urls = prj.check_urls(urls)
    print(valid_urls)
    print(not_valid_urls)
    data = prj.get_reviews_by_label('A', 19)
    print(data)
    urls = prj.get_urls_not_processed(18)
    print(urls)
    a = prj.get_project_models(5)
    print(a)
