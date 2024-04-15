from flask import Blueprint, jsonify
from models.top_recommendation import top_movies

top_movies_blueprint = Blueprint('top_movies_api', __name__)

def create_top_movies_api(processed_data):
    @top_movies_blueprint.route('/top_movies', methods=['GET'])
    def get_top_movies():
        # Get top movies
        top_movies_data = top_movies(processed_data)
        top_10_movies = top_movies_data.head(10)
        return top_10_movies.to_json(orient='records')

    return top_movies_blueprint
