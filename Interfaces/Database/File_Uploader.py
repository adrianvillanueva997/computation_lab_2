from Database.ETL import File_Manager
from Database import config as cfg


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
                    ut = utilities.Utilities()
                    review = ut.scrape_text_for_sql(review)
                    file_name = ut.scrape_text_for_sql(file_names[index])
                    query = f'INSERT INTO proyecto_computacion.review (ID_project,text_review,file_name,label) ' \
                        f'values ({self.project_id}, \"{review}\" ,\"{file_name}\",\"{label}\")'
                    con.execute(query)
                    print(query)
                    index += 1
                except Exception as e:
                    self.failed_file_names.append(file_names[index])
                    self.failed_reviews.append(review)
                    print(e)


if __name__ == '__main__':
    fm = File_Manager.File_Manager()
    good_reviews, g_file_names = fm.extract_data_from_files(
        '/home/xiao/Downloads/dataset_entrenamiento/buenas')
    fp = File_Uploader(19)
    fp.upload_reviews_to_db(good_reviews, g_file_names)
