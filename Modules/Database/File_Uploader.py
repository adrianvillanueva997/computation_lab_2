from sqlalchemy.sql import text

from Modules.Database import Utilities
from Modules.Database import config as cfg


class File_Uploader:
    def __init__(self, project_id):
        """
        Class constructor, receives the project ID
        :param project_id:
        """
        self.project_id = project_id
        self.failed_reviews = []
        self.failed_file_names = []

    def upload_reviews_to_db(self, reviews, file_names, label):
        """
        Receives 2 lists with strings and uploads them to the database associating them to the project id given to the object
        :param reviews:
        :param file_names:
        :return:
        """
        with cfg.engine.connect() as con:
            index = 0
            for review in reviews:
                # file_name | text_review
                try:
                    ut = Utilities.Utilities()
                    review = ut.scrape_text_for_sql(review)
                    file_name = ut.scrape_text_for_sql(file_names[index])
                    query = text('INSERT INTO proyecto_computacion.review (ID_project,text_review,file_name,label) '
                                 f'values (:_project_id, :_review ,:_file_name,:_label)')
                    con.execute(query, _project_id=self.project_id, _review=review, _file_name=file_name, _label=label)
                    print(query)
                    index += 1
                except Exception as e:
                    self.failed_file_names.append(file_names[index])
                    self.failed_reviews.append(review)
                    print(e)

    def upload_single_review_to_db(self, name, label, review):
        """
        Receives 2 lists with strings and uploads them to the database associating them to the project id given to the object
        :param text:
        :param label:
        :param name:
        :return:
        """
        with cfg.engine.connect() as con:
            try:
                query = text("INSERT INTO proyecto_computacion.review (ID_project,label,file_name,text_review) " \
                             "values (:a,:b,:c,:d)")
                con.execute(query, a=self.project_id, b=label, c=name, d=review)
                print(query)
            except Exception as e:
                print(e)
