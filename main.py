from flask import Flask, jsonify
import pandas as pd
from Models.top_recommendation import preprocess_data, top_movies
from Models.collab_recommendation import user_based_collaborative_filtering
from Models.collab_preprocess import collab_preprocess_data

app = Flask(__name__)

# Load data
movies_df = pd.read_csv('./Data/movies_metadata.csv')
movies_poster_path = pd.read_csv('./Data/movies_metadata_with_poster_path.csv')

movies_df = pd.merge(movies_df, movies_poster_path[['id', 'new_poster_path']], on='id', how='left')

ratings_df = pd.read_csv('./Data/ratings_small.csv')
links_df = pd.read_csv('./Data/links_small.csv')

# Preprocess data
processed_data = preprocess_data(movies_df)
collab_df = collab_preprocess_data(movies_df, ratings_df, links_df)

# User-based Collaborative Filtering
users_choice, common = user_based_collaborative_filtering(collab_df)

@app.route('/user_ids', methods=['GET'])
def get_user_ids():
    try:
        user_ids = collab_df['userId'].unique().tolist()
        return jsonify({'user_ids': user_ids})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/recommendations/<int:user_id>', methods=['GET'])
def get_recommendations(user_id):
    try:
        user_favourite_films_df = users_choice(user_id)
        user_favourite_films = user_favourite_films_df.to_dict(orient='records')
        recommended_films = common(user_id)
        return jsonify({'user_favourite_films': user_favourite_films, 'recommended_films': recommended_films})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/top_movies', methods=['GET'])
def get_top_movies():
    # Get top movies
    top_movies_data = top_movies(processed_data)
    # Get only the top 10 movies
    top_10_movies = top_movies_data.head(10)
    # Convert DataFrame to JSON and return
    return top_10_movies.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)