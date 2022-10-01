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
    if index != "Rating" and index != "Popularity Index":
        return "Invalid index or type"
    
    type_list = ["count", "mean", "median", "min", "max"]
    
    if type not in type_list:
        return "Invalid index or type"
        
    def transform(x):
        '''
        Turn a string separated by , into its numerical value
        '''
        parsed = ""
        while x.find(",") != -1:
            parsed += x[: x.find(",")]
            x = x[x.find(",") + 1:]
        parsed += x
        return int(parsed)
    
    df = get_movies_data()
    
    if index == "Popularity Index":
        # Need to perform a transformation on Popularity index
        # because it is not a numerical value 
        df['Popularity Index n'] = df[index].apply(transform)
    
        index = "Popularity Index n"
        
    output = 0
    
    if type == "count":
        output = df[index].count()
    elif type == "mean":
        output = df[index].mean()
    elif type == "median":
        output = df[index].median()
    elif type == "min":
        output = df[index].min()
    else:
        output = df[index].max()
    
    return round(output, 2)

def get_actor_movies_release_year_range(actor, upper, lower=0):
    if lower > upper:
        raise ValueError
    
    df = get_movies_data()
    
    played_in = df['Movie Cast'].str.contains(actor)
    
    played_in_df = df[played_in]
    
    played_in_df = played_in_df[(played_in_df['Year of Release'] >= lower) & (played_in_df['Year of Release'] <= upper)]

    # Need to return a Series object with title as indices, and year as the value
    ret = pd.Series(played_in_df['Year of Release'].values, index=played_in_df['Title'])
    
    return ret    

def get_actor_median_rating(actor):
    pass

def get_directors_median_reviews():
    pass
