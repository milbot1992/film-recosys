import pandas as pd
import re
import numpy as np

def load_data():
    movies_df = pd.read_csv('./Data/movies_metadata.csv')
    ratings_df = pd.read_csv('./Data/ratings_small.csv')
    links_df = pd.read_csv('./Data/links_small.csv')
    return movies_df, ratings_df, links_df

def convert_int(x):
    try:
        return int(x)
    except:
        return np.nan

def collab_preprocess_data(movies_df, ratings_df, links_df):
    
    movies_df = movies_df.drop([19758 , 29543, 35630])
    
    movies_df['id'] = movies_df['id'].astype('int')

    small_movies_df = movies_df[movies_df['id'].isin(links_df['movieId'])]
    
    df = small_movies_df.merge(ratings_df, left_on='id', right_on='movieId')

    # Drop users who vote less than 200 times.
    collab_df = df[df['userId'].map(df['userId'].value_counts()) > 150]
    
    return collab_df