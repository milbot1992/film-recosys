import requests
from flask import Blueprint, jsonify
from utils.image_utils import get_image_url

trending_now_api = Blueprint('trending_now_api', __name__)

@trending_now_api.route('/trending_now', methods=['GET'])
def get_trending_now():
    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzYyMWQ1YTM2MTA1NjEwYzc1OWZmOWM3YjY3ODQ5YiIsInN1YiI6IjY2MTY4OWEzY2U1ZDgyMDE3YzkwM2MwNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wsDnNvPxLXf0Y5UEXHKVAz4qKk9HIAg4DguddcUAATQ"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        trending_movies = response.json().get('results')[:10]  # Get top 10 trending movies
        
        # Transform the response to match the desired format
        formatted_response = []
        for movie in trending_movies:
            formatted_movie = {
                "title": movie["title"],
                "year": movie["release_date"].split("-")[0],
                "vote_count": movie["vote_count"],
                "vote_average": movie["vote_average"],
                "popularity": movie["popularity"],
                "poster_url": get_image_url(movie["poster_path"])
            }
            formatted_response.append(formatted_movie)
        
        return jsonify({'trending_movies': formatted_response})
    else:
        return jsonify({'error': 'Failed to fetch trending movies'}), response.status_code
