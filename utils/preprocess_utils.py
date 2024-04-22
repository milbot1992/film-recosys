import pandas as pd
import logging
from models.collab_preprocess import collab_preprocess_data
from utils.image_utils import get_image_url

def load_and_preprocess_data():
    """
    Load movie data from CSV files, merge metadata with poster path,
    preprocess the data for collaborative filtering, and return the resulting DataFrame.

    Returns:
        pd.DataFrame: The preprocessed movie data ready for collaborative filtering.
    """
    logging.info("Loading and preprocessing data...")

    logging.info("Loading movies metadata...")
    movies_df = pd.read_csv('./Data/movies_metadata.csv')
    movies_df = movies_df.drop([19730 , 29503, 35587])
    movies_poster_path = pd.read_csv('./Data/movies_metadata_with_poster_path.csv')
    movies_poster_path = movies_poster_path.drop([12735 , 12899, 12922])

    # Ensure 'movie_id' is an int
    movies_df['movie_id'] = movies_df['movie_id'].astype('int')
    movies_poster_path['movie_id'] = movies_poster_path['movie_id'].astype('int')

    # Create a new column 'new_full_image_url' using get_image_url function
    movies_poster_path['new_full_image_url'] = movies_poster_path['new_poster_path'].apply(get_image_url)

    logging.info("Merging movie metadata with poster path...")
    movies_df = pd.merge(movies_df, movies_poster_path[['movie_id', 'new_full_image_url']], on='movie_id', how='left')
    logging.info("Loading ratings data...")
    ratings_df = pd.read_csv('./Data/ratings_small.csv')
    links_df = pd.read_csv('./Data/links_small.csv')

    logging.info("Preprocessing data...")
    collab_df = collab_preprocess_data(movies_df, ratings_df, links_df)

    logging.info("Data loading and preprocessing completed.")

    return collab_df
