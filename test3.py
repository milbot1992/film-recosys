import pandas as pd
import requests

# API key obtained from TMDB
api_key = '3c621d5a36105610c759ff9c7b67849b' 

# Function to fetch poster path for a given movie ID
def get_poster_path(movie_id, api_key):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print('>>>>>', data)
        return data.get('poster_path') 
    else:
        print(f"Failed to fetch data for movie ID {movie_id}. Status code:", response.status_code)
        return None

get_poster_path(913,api_key)