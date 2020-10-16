from flask import Flask, jsonify, request, json
import joblib
import pandas as pd


app = Flask(__name__)

app.config['SECRET_KEY'] = 'KEY'

#rutas raiz
@app.route('/movies', methods=['POST'])
def recommended():
    try:
        cosine_sim = joblib.load("./models/modelCosine.pkl")
        df_movies = pd.read_csv('./data/df_movies.csv')
        indices = pd.Series(df_movies['id'])
        req_data = request.get_json(force=True)
        indice = int(req_data['id_title'])
        
        recommended_movies = []
        idx = int(indices[indices == indice].index[0])
        score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)
        top5_indexes = list(score_series.iloc[1:6].index)

        for i in top5_indexes:
            recommended_movies.append(dict(df_movies.iloc[i]))
        print(recommended_movies)
        return jsonify(recommended_movies)
    except IndexError:
        return jsonify([])


if __name__ == "__main__":
    app.run(port=5000)