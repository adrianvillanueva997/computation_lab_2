import pandas as pd

try:
    from Interfaces.Database.ETL.Modules import Vectorizer
    from Interfaces.Database.ETL.Modules.Models import Models
except Exception as e:
    # ADRI METE AQUI TUS IMPORTS
    pass


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

        :param reviews_dict:
        :param transformer:
        :param algorithm:
        :return:
        """
        data_frame = self.__generate_reviews_dataframe(reviews_dict)
        vect = Vectorizer.Vectorizer()
        print(transformer)
        print(data_frame['reviews'])
        x_train, x_test, y_train, y_test = vect.generate_train_test_data(data_frame=data_frame, vectorizer=transformer)
        model = Models(x_train=x_train, x_test=x_test, y_train=y_train, y_test=y_test, vectorizer=vect)
        model = self.__algorithm_choser(algorithm, model)
        return model

    @staticmethod
    def __algorithm_choser(algorithm, model):
        """

        :param algorithm:
        :param model:
        :return:
        """
        if algorithm is 'tree_classification':
            model.tree_decision_classifier()
        elif algorithm is 'tree_extra_classification':
            model.tree_extra_tree_classifier()
        elif algorithm is 'tree_random_forest':
            model.tree_random_forest()
        elif algorithm is 'bayes_multinomial':
            model.naive_bayes_multinomial()
        elif algorithm is 'bayes_bernouilli':
            model.naive_bayes_bernoulli()
        elif algorithm is 'bayes_gaussian':
            model.naive_bayes_gaussian()
        elif algorithm is 'ada_classification':
            model.ada_classifier()
        elif algorithm is 'gradient_booster':
            model.gradient_booster()
        elif algorithm is 'gradient_stochastic':
            model.gradient_stochastic_descent()
        elif algorithm is 'neighbours_k':
            model.k_neighbors_classifier()
        elif algorithm is 'neighbours_radius':
            model.r_neighbors_classifier()
        elif algorithm is 'svm_classification':
            model.svm_support_vector_classification()
        elif algorithm is 'svm_nu_classification':
            model.svm_support_vector_nu_classification()
        elif algorithm is 'svm_linear_classification':
            model.svm_support_vector_linear_classification()
        elif algorithm is 'neural_mlp':
            model.neural_sklearn_mlp()
        elif algorithm is 'gaussian_classifier':
            model.gaussian_process_classifier()

        return model
