import requests

url = "https://api.themoviedb.org/3/movie/11788?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzYyMWQ1YTM2MTA1NjEwYzc1OWZmOWM3YjY3ODQ5YiIsInN1YiI6IjY2MTY4OWEzY2U1ZDgyMDE3YzkwM2MwNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wsDnNvPxLXf0Y5UEXHKVAz4qKk9HIAg4DguddcUAATQ"
}

response = requests.get(url, headers=headers)

print(response.text)