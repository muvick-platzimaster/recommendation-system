
import pandas as pd
#app
from connection import db


def _query_movies(db=db):

    movies = db.movies
    cursor_movies = movies.find( { } )

    return cursor_movies


def _dataframe_movies():

    cursor_movies = _query_movies()
    df_movies = pd.DataFrame(cursor_movies)

    return df_movies


if __name__ == "__main__":
    
    df_movies = _dataframe_movies()
    df_movies.to_csv('./df_movies.csv', index=False)