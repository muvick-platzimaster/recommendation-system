from modeling import cosine_sim
from transform_data import df_idx

import pandas as pd


def recommendations(title, cosine_sim=cosine_sim, df_idx=df_idx()):

    try:
        recommended = []
        idx = df_idx[df_idx['original_title']==title].index[0]
        score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)

        return score_series
    except IndexError:
        return []


if __name__ == "__main__":
    result = recommendations('Mulan')
    print(result)