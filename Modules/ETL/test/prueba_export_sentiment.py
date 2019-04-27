try:
    from ETL import Models, Vectorizer, File_Manager, Sentiment
except Exception as e:
    import Models, Vectorizer, File_Manager

fm = File_Manager.File_Manager()
unlabeled_reviews, u_file_names = fm.extract_data_from_files(
    r'/home/xiao/Downloads/dataset_entrenamiento/unlabeled')

sent = Sentiment.Sentiment()

Texto = ['I dont feel good', 'Please give me some tea', 'I dont like this test',
         'This game is so bad that it gave me cancer']
sent.analyse_texts(Texto)
sent.export_sentiment_to_csv(path='', file_name='g_reviews')
