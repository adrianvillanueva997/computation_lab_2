import pandas as pd

from Modules.ETL.Model_Importer import Model_Importer


class Classify:
    def __init__(self):
        self.model = None
        self.vectorizer = None
        self.dataframe = None

    @staticmethod
    def __generate_model_object(project_id, model_id):
        model_importer = Model_Importer()
        model = model_importer.load_model(project_id, model_id)
        return model

    @staticmethod
    def __generate_unlabeled_dataframe(unlabeled_dict):
        df = pd.DataFrame(unlabeled_dict)
        return df

    def classify(self, unlabeled_dict, project_id, model_id):
        self.model = self.__generate_model_object(project_id, model_id)
        self.dataframe = self.__generate_unlabeled_dataframe(unlabeled_dict)
        vectorizer = self.model.vectorizer.get_vectorizer()
        vectorized_dataframe = vectorizer.transform(self.dataframe['reviews'])
        prediction = self.model.predict(vectorized_dataframe)
        print(prediction)
        print(len(prediction))
        print(self.dataframe)
        self.dataframe['labels'] = prediction
        return self.dataframe
