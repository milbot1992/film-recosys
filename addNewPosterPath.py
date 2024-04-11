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
        return data.get('poster_path') 
    else:
        print(f"Failed to fetch data for movie ID {movie_id}. Status code:", response.status_code)
        return None

# Load the movies_metadata.csv file into a DataFrame
file_path = './Data/movies_metadata.csv'
movies_df = pd.read_csv(file_path)
movies_df = movies_df.sort_values(by='id', ascending=True)

# Iterate through each row in movies_df and fetch poster path using the id
for index, row in movies_df.iterrows():
    movie_id = row['id']
    print('movie_id :', movie_id)
    poster_path = get_poster_path(movie_id, api_key)
    movies_df.at[index, 'new_poster_path'] = poster_path

print('movies_df_cols: ', movies_df.columns)
print('movies_df: ', movies_df)

# Save the updated DataFrame to a new CSV file with the new column
output_file_path = 'movies_metadata_with_poster_path.csv'
movies_df.to_csv(output_file_path, index=False)

print(f"New CSV file saved with poster paths: {output_file_path}")