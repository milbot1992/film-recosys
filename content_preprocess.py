import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

def load_data():
    links_small = pd.read_csv('./Data/links_small.csv')
    links_small = links_small[links_small['tmdbId'].notnull()]['tmdbId'].astype('int')
    movies_data = pd.read_csv('./Data/movies_metadata.csv')
    return links_small, movies_data

def preprocess_data(movies_data, links_small):
    smd = movies_data[movies_data['id'].isin(links_small)]
    smd['tagline'] = smd['tagline'].fillna('')
    smd['description'] = smd['overview'] + smd['tagline']
    smd['description'] = smd['description'].fillna('')
    return smd