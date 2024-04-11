from flask import Blueprint, jsonify
from ..Models.top_recommendation import top_movies
from ..Utils.preprocess_utils import processed_data

top_movies_api = Blueprint('top_movies_api', __name__)

# Get top movies
top_movies_data = top_movies(processed_data)
top_10_movies = top_movies_data.head(10)

@top_movies_api.route('/top_movies', methods=['GET'])
def get_top_movies():
    return top_10_movies.to_json(orient='records')