import pandas as pd
import re
import numpy as np
import logging

def load_data():
    """
    Load movie data from CSV files and return DataFrames for movies, ratings, and links.

    Returns:
        tuple: A tuple containing three DataFrames for movies, ratings, and links, respectively.
    """
    logging.info("Loading data...")

    movies_df = pd.read_csv('./Data/movies_metadata.csv')
    ratings_df = pd.read_csv('./Data/ratings_small.csv')
    links_df = pd.read_csv('./Data/links_small.csv')

    logging.info("Data loaded successfully.")

    return movies_df, ratings_df, links_df

def convert_int(x):
    try:
        return int(x)
    except:
        return np.nan

def collab_preprocess_data(movies_df, ratings_df, links_df):
    """
    Preprocess movie data for collaborative filtering.

    Args:
        movies_df (pd.DataFrame): DataFrame containing movie metadata.
        ratings_df (pd.DataFrame): DataFrame containing movie ratings.
        links_df (pd.DataFrame): DataFrame containing movie links.

    Returns:
        pd.DataFrame: Preprocessed movie data for collaborative filtering.
    """
    logging.info("Preprocessing data...")

    # Convert 'movie_id' column to integer
    movies_df['movie_id'] = movies_df['movie_id'].astype('int')

    # Filter movies DataFrame based on links DataFrame
    small_movies_df = movies_df[movies_df['movie_id'].isin(links_df['movieId'])]

    # Merge movies and ratings DataFrames
    df = small_movies_df.merge(ratings_df, left_on='movie_id', right_on='movieId')

    # Drop users who vote less than 200 times
    collab_df = df[df['userId'].map(df['userId'].value_counts()) > 150]

    logging.info("Data preprocessing completed.")

    return collab_df
