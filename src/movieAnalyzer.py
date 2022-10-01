# Run this script from the repository's root.

import os
import pandas as pd
top200_movies_file = os.path.join('src', 'data', 'Top_200_Movies.csv')

def get_movies_data():
    return pd.read_csv(top200_movies_file)

def get_movies_interval(y1, y2):
    if y1 > y2:
        raise ValueError
    
    df = get_movies_data()
    
    required_df = df[(df['Year of Release'] >= y1) & (df['Year of Release'] <= y2)]
    
    return required_df['Title']

def get_rating_popularity_stats(index, type):
    pass

def get_actor_movies_release_year_range(actor, upper, lower=0):
    pass

def get_actor_median_rating(actor):
    pass

def get_directors_median_reviews():
    pass
