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
        if pd.isnull(x):
            return x
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
    
    return f"{output:.2f}"

def get_actor_movies_release_year_range(actor, upper, lower=0):
    if lower > upper:
        raise ValueError
    
    df = get_movies_data()
    
    def transform(x, actor):
        if pd.isnull(x):
            return False
        x = x.strip("[],")
        splitted = x.split(",")
        
        for split in splitted:
            stripped = split.strip("' ") # Strip away the hypo and space
            if stripped == actor:
                return True
        return False
    
    played_in = df['Movie Cast'].apply(transform, actor=actor)
    
    played_in_df = df[played_in]
    
    played_in_df = played_in_df[(played_in_df['Year of Release'] >= lower) & (played_in_df['Year of Release'] <= upper)]

    # Need to return a Series object with title as indices, and year as the value
    ret = pd.Series(played_in_df['Year of Release'].values, index=played_in_df['Title'])
    
    return ret    

def get_actor_median_rating(actor):
    if actor == "":
        raise ValueError
    elif type(actor) != str:
        raise TypeError
    
    df = get_movies_data()
    
    def transform(x, actor):
        if pd.isnull(x):
            return False
        x = x.strip("[],")
        splitted = x.split(",")
        
        for split in splitted:
            stripped = split.strip("' ") # Strip away the hypo and space
            if stripped == actor:
                return True
        return False
    
    played_in = df['Movie Cast'].apply(transform, actor=actor)
    
    played_in_df = df[played_in]
    
    if played_in_df.empty:
        return None
    return played_in_df['Rating'].median()

def get_directors_median_reviews():
    # Need to transform the Number of Reviews column into float
    # and it needs to be out of millions
    def transform(x):
        if type(x) != str:
            return 0
        if x[-1] == 'K':
            return float(x[:-1]) / 1000
        elif x[-1] == 'M':
            return float(x[:-1])
        else:
            # No units return 0
            return float(0)
    
    df = get_movies_data()
    
    df['Reviews'] = df['Number of Reviews'].apply(transform)
    
    ret = df.groupby('Director')['Reviews'].median()
    
    return ret
