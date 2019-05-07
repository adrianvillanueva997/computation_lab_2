import pandas as pd

from Modules.ETL.Modules import Models
from Modules.ETL.Modules import Vectorizer


class Train:
    def __init__(self):
        pass

    @staticmethod
    def __generate_reviews_dataframe(reviews_dict):
        """

        :param reviews_dict:
        :return:
        """
        df = pd.DataFrame(data=reviews_dict)
        return df

    def trainer(self, reviews_dict, transformer, algorithm):
        """

        :rtype:
        :param reviews_dict:
        :param transformer:
        :param algorithm:
        :return:
        """
        data_frame = self.__generate_reviews_dataframe(reviews_dict)
        vect = Vectorizer.Vectorizer()
        x_train, x_test, y_train, y_test = vect.generate_train_test_data(data_frame=data_frame, vectorizer=transformer)
        model = Models.Models(x_train=x_train, x_test=x_test, y_train=y_train, y_test=y_test, vectorizer=vect)
        model = self.__algorithm_choser(algorithm, model)
        return model

    @staticmethod
    def __algorithm_choser(algorithm, model):
        """

        :param algorithm:
        :param model:
        :return:
        """
        if algorithm == 'Classification Trees':
            model.tree_decision_classifier()
        elif algorithm == 'Extra-Classification Trees':
            model.tree_extra_tree_classifier()
        elif algorithm == 'Random Forest':
            model.tree_random_forest()
        elif algorithm == 'Naive Bayes Multinomial':
            model.naive_bayes_multinomial()
        elif algorithm == 'Naive Bayes Bernoulli':
            model.naive_bayes_bernoulli()
        elif algorithm == 'Naive Bayes Gaussian':
            model.naive_bayes_gaussian()
        elif algorithm == 'Ada Classification':
            model.ada_classifier()
        elif algorithm == 'Gradient Boosted Trees':
            model.gradient_booster()
        elif algorithm == 'Stochastic Gradient Boosted':
            model.gradient_stochastic_descent()
        elif algorithm == 'K-nn':
            model.k_neighbors_classifier()
        elif algorithm == 'Radius Neighbors Classifier':
            model.r_neighbors_classifier()
        elif algorithm == 'SVM Classification':
            model.svm_support_vector_classification()
        elif algorithm == 'SVM Nu-Classification':
            model.svm_support_vector_nu_classification()
        elif algorithm == 'SVM Linear Classification':
            model.svm_support_vector_linear_classification()
        elif algorithm == 'Neural Network MLP':
            model.neural_sklearn_mlp()
        elif algorithm == 'Gaussian Classifier':
            model.gaussian_process_classifier()

        return model
