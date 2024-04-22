import pytest
import requests

@pytest.fixture
def api_url():
    return 'http://localhost:5000'

def test_user_api(api_url):
    response = requests.get(f'{api_url}/user')
    assert response.status_code == 200
    response_json = response.json()
    
    # Check if the response is a list format
    assert isinstance(response_json['user_ids'], list)
    
    # Check if there are 10 or more user IDs
    assert len(response_json['user_ids']) >= 10


def test_trending_now_api(api_url):
    response = requests.get(f'{api_url}/trending_now')
    assert response.status_code == 200
    response_json = response.json()
    
    # Check if the response contains the 'trending_movies' key
    assert 'trending_movies' in response_json
    
    # Check if the value of 'trending_movies' is a list
    assert isinstance(response_json['trending_movies'], list)
    
    # Check if there are exactly 10 movies in the response
    assert len(response_json['trending_movies']) == 10
    
    # Check if each movie in the list contains the required keys
    for movie in response_json['trending_movies']:
        assert all(key in movie for key in ['popularity', 'poster_path', 'title', 'vote_average', 'vote_count', 'year'])


def test_recommendations_api(api_url):
    response = requests.get(f'{api_url}/recommendations')
    assert response.status_code == 200
    response_json = response.json()
    
    # Check if all expected keys are present in the response
    expected_response_keys = ['recommended_films', 'user_favourite_films']
    assert all(key in response_json for key in expected_response_keys)
    
    # Check if each key contains a list of 5 items
    for key in expected_response_keys:
        assert isinstance(response_json[key], list)
        assert len(response_json[key]) == 5

