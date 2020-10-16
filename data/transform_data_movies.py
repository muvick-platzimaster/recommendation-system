
#libraries
from rake_nltk import Rake
import pandas as pd
import re



df_movies = pd.read_csv('./df_movies.csv')
df_model_movies = df_movies[['id','genres','overview']]


def words_genres(row):
    match = re.compile(r'[A-Z][a-z]+')
    words = match.findall(row['genres'])

    return words


def key_words(row):
    rake = Rake()
    rake.extract_keywords_from_text(row['overview'])
    key_words_dict_scores = rake.get_word_degrees()

    return list(key_words_dict_scores.keys())


def transform_df(df=df_model_movies):

    df_movies = pd.read_csv('./df_movies.csv')
    df_model_movies = df_movies[['id','genres','overview']]

    df_model_movies['genres'] = df_model_movies.apply(words_genres, axis=1)
    df_model_movies = df_model_movies.set_index(['id'])
    #key words from overview
    df_model_movies['key_words'] = df_model_movies.apply(key_words, axis=1)
    df_model_movies.drop(columns=['overview'], inplace=True)

    return df_model_movies


def bag_words():

    df_model_movies = transform_df()

    # unite all the features in a single basket of words
    df_model_movies['bag_of_words'] = ''
    columns = df_model_movies.columns

    for _, row in df.iterrows():
        words = ''
        for col in columns:
            words = words + ' '.join(row[col]) + ' '
        row['bag_of_words'] = words

    df_model_movies.drop(columns=[col for col in df_model_movies if col != 'bag_of_words'], inplace=True)

    return df_model_movies




