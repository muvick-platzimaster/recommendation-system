# app
from transform_data_movies import bag_words
import pandas as pd
#libraries
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import joblib


df_model_movies = bag_words()
count = CountVectorizer()
count_matrix = count.fit_transform(df_model_movies['bag_of_words'])

cosine_sim = cosine_similarity(count_matrix, count_matrix)
joblib.dump(cosine_sim, './model_training.pkl')

