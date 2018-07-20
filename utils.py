import pandas as pd
import json

def extract_name(row):
    return [genre['name'] for genre in json.loads(row)]


def read_movie_data(start_year=2012, end_year=2016):
    df = pd.read_csv('data/tmdb_5000_movies.csv')

    df['genres'] = df.genres.apply(extract_name)
    df['production_countries'] = df.production_countries.apply(extract_name)
    df['release_date'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d')
    df['release_year'] = df.release_date.dt.year.fillna(0).astype(int)

    df['genre'] = df.genres.apply(lambda x: x[0] if len(x) > 0 else 'None')
    df['production_country'] = df.production_countries.apply(lambda x: x[0] if len(x) > 0 else 'None')

    df = df[['budget', 
             'genre',
             'original_language', 
             'title',
             'production_country',
             'release_date',
             'revenue',
             'runtime',
             'vote_average',
             'vote_count',
             'release_year'
            ]]

    return df[df.release_year.between(start_year, end_year)]
