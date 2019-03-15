from Database import config as cfg
from ETL import File_Manager


class File_Uploader:
    def __init__(self, project_id):
        """
        Class constructor, receives the project ID
        :param project_id:
        """
        self.project_id = project_id
        self.failed_reviews = []
        self.failed_file_names = []

    def upload_reviews_to_db(self, reviews, file_names):
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
                    review = str(review).replace('\'', '\'\'')
                    review = review.replace('\"', '\"\"')
                    review = review.replace('%', '%%')
                    file_name = str(file_names[index]).replace('\'', '\'\'')
                    file_name = file_name.replace('\"', '\"\"')

                    query = f'INSERT INTO proyecto_computacion.review (ID_project,text_review,file_name) values ({self.project_id}, \"{review}\" ,\"{file_name}\")'
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
        '/home/xiao/Downloads/dataset_entrenamiento/buenas/')
    fp = File_Uploader(17)
    fp.upload_reviews_to_db(good_reviews, g_file_names)
