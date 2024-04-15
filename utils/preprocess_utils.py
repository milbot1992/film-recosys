import pandas as pd
from models.collab_preprocess import collab_preprocess_data

def load_and_preprocess_data():
    # Load data
    movies_df = pd.read_csv('./Data/movies_metadata.csv')
    movies_poster_path = pd.read_csv('./Data/movies_metadata_with_poster_path.csv')

    # Merge movie metadata with poster path
    movies_df = pd.merge(movies_df, movies_poster_path[['id', 'new_poster_path']], on='id', how='left')

    ratings_df = pd.read_csv('./Data/ratings_small.csv')
    links_df = pd.read_csv('./Data/links_small.csv')

    # Preprocess data
    collab_df = collab_preprocess_data(movies_df, ratings_df, links_df)

    return collab_df