import pandas as pd
#app
from connection import db


def _query_series(db=db):

    series = db.series
    cursor_series = series.find( { } )

    return cursor_series


def _dataframe_series():

    cursor_series = _query_series()
    df_series = pd.DataFrame(cursor_series)

    return df_series


if __name__ == "__main__":
    
    df_series = _dataframe_series()
    df_series.to_csv('./df_series.csv', index=False)