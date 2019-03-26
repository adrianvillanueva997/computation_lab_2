import uuid

try:
    from Database import config as cfg
    from Database import User
    from .ETL import Sentiment, Models, Vectorizer, File_Manager
except Exception as e:
    from Interfaces.Database import config as cfg, Utilities
    from Interfaces.Database import User
    from Interfaces.Database.ETL import Sentiment, Models, Vectorizer, File_Manager


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

                query = f'SELECT * from proyecto_computacion.review WHERE ID_project LIKE {project_id}'
                results = con.execute(query)
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
                query = f'SELECT * FROM proyecto_computacion.project prj join proyecto_computacion.review ' \
                    f'on prj.ID_project = review.ID_project where prj.ID_project like {project_id} and sentiment_pol is null'
                results = con.execute(query)
                for result in results:
                    try:
                        review_id = result['ID_review']
                        text = result['text_review']
                        sentiments = sentiment.analyse_sentence(text)
                        update_query = f"update proyecto_computacion.review set " \
                            f"sentiment_pol = {sentiments['polarity'][0]}," \
                            f"sentiment_sub = {sentiments['subjectivity'][0]}," \
                            f"sentiment_comp = {sentiments['compound'][0]} " \
                            f"where ID_review like {review_id}"
                        con.execute(update_query)
                    except Exception as e:
                        print(e)
                        failed_reviews.append(text)
                        self.failed_reviews = failed_reviews
        except Exception as e:
            print(e)

    def classify_reviews(self, model, project_id):
        """
        Given a trained sklearn model, execute the model to classify the reviews that haven't been classified yet.
        TODO re-do the logic and think an alternative version to this.
        :param model:
        :param project_id:
        :return:
        """
        try:
            with cfg.engine.connect() as con:
                query = f'SELECT * FROM proyecto_computacion.project prj join proyecto_computacion.review ' \
                    f'on prj.ID_project = review.ID_project where prj.ID_project like {project_id} and label is null'
                results = con.execute(query)
                failed_reviews = []
                for result in results:
                    try:
                        review_id = result['ID_review']
                        text = result['text_review']
                        prediction = model.predict(text)
                        update_query = f'update proyecto_computacion.review set ' \
                            f'label = {prediction[0]} where ID_review = {review_id}'
                        print(update_query)
                        con.execute(update_query)
                    except Exception as e:
                        failed_reviews.append(text)
                        self.failed_reviews_label = failed_reviews
                        print(e)
        except Exception as e:
            print(e)

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
                        query = f'insert into proyecto_computacion.Label' \
                            f' (label, ID_Project) VALUES (\"{label}\",{project_id});'
                        print(query)
                        con.execute(query)
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
                        query = f'INSERT INTO proyecto_computacion.link_web_scrapper (ID_project, url, processed) ' \
                            f'values ({project_id},\"{url}\",0)'
                        con.execute(query)
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
                query = f'SELECT * FROM proyecto_computacion.Label where ID_Project like {project_id}'
                results = con.execute(query)
                labels = []
                for result in results:
                    labels.append(result['label'])
            return labels
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
                query = f'SELECT * FROM proyecto_computacion.review where label like \"{label}\" and  ID_project like {project_id}'
                results = con.execute(query)
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
                query = f'select * from proyecto_computacion.link_web_scrapper ' \
                    f'where processed like 0 and ID_project like {project_id}'
                results = con.execute(query)
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
                query = f'select * from proyecto_computacion.link_web_scrapper ' \
                    f'where processed like 1 and ID_project like {project_id}'
                results = con.execute(query)
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
                query = f'UPDATE proyecto_computacion.link_web_scrapper set processed 1 ' \
                    f'where url like \"{url}\" and ID_project like {project_id}'
                con.execute(query)
        except Exception as e:
            print(e)

    @staticmethod
    def __get_url_id(url, project_id):
        try:
            with cfg.engine.connect() as con:
                query = f'SELECT * from proyecto_computacion.link_web_scrapper where url like \"{url}\" and ID_project like {project_id}'
                results = con.execute(query)
                id = ''
                for result in results:
                    id = result['ID_link']
            return id
        except Exception as e:
            print(e)

    def upload_scrapped_review(self, project_id, reviews, url):
        # TODO
        pass


if __name__ == '__main__':
    user = User(10)
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
