import pytest
import sys, os
sys.path.insert(1, os.getcwd())
from src.movieAnalyzer import pd, get_movies_interval, get_rating_popularity_stats, get_actor_movies_release_year_range, get_actor_median_rating, get_directors_median_reviews, get_movies_data

class TestMovieAnalyzer:
    def setup_method(self):
        self.df = get_movies_data()
    
    def test_get_movie_interval1(self):
        ret = get_movies_interval(1992, 1993)
        
        exp = pd.Series(["Schindler's List", 'Reservoir Dogs', 'Unforgiven', 'Jurassic Park', 'In the Name of the Father', 'Groundhog Day'],
                        index=[5, 88, 131, 141, 177, 205], name="Title")
        
        assert ret.equals(exp)
        assert ret.name == exp.name
    
    def test_get_movie_interval2(self):
        ret = get_movies_interval(2000, 2000)

        exp = pd.Series(['Gladiator', 'Memento', 'Requiem for a Dream', 'Snatch'],
                        index=[36, 52, 81, 113], name="Title")
        
        assert ret.equals(exp)
        assert ret.name == exp.name
    
    def test_get_movie_interval3(self):
        ret = get_movies_interval(2020, 2020)
        
        exp = pd.Series(['Hamilton', 'The Father'],
                        index=[115, 126], name="Title")
        
        assert ret.equals(exp)
        assert ret.name == exp.name
    
    def test_get_movie_interval4(self):
        ret = get_movies_interval(2023, 2023)
        
        exp = pd.Series([], name="Title", dtype=object)
        
        assert ret.equals(exp)
        assert ret.name == exp.name
    
    def test_get_movie_interval5(self):
        with pytest.raises(ValueError):
            ret = get_movies_interval(2025, 2020)
        
    def test_get_stat1(self):
        assert get_rating_popularity_stats("Popularity Index", "count") == 207
    
    def test_get_stat2(self):
        assert get_rating_popularity_stats("Popularity Index", "min") == 3
    
    def test_get_stat3(self):
        assert get_rating_popularity_stats("Popularity Index", "max") == 4940
    
    def test_get_stat4(self):
        assert get_rating_popularity_stats("Popularity Index", "mean") == 1091.92
    
    def test_get_stat5(self):
        assert get_rating_popularity_stats("Popularity Index", "median") == 673.0
    
    def test_get_stat6(self):
        assert get_rating_popularity_stats("Rating", "count") == 207
    
    def test_get_stat7(self):
        assert get_rating_popularity_stats("Rating", "min") == 8.1
    
    def test_get_stat8(self):
        assert get_rating_popularity_stats("Rating", "max") == 9.3
    
    def test_get_stat9(self):
        assert get_rating_popularity_stats("Rating", "mean") == 8.34
    
    def test_get_stat10(self):
        assert get_rating_popularity_stats("Rating", "median") == 8.3
    
    def test_get_stat11(self):
        assert get_rating_popularity_stats("Ratingx", "median") == "Invalid index or type"
    
    def test_get_stat12(self):
        assert get_rating_popularity_stats("Rating", "hehe") == "Invalid index or type"
    
    def test_get_stat13(self):
        assert get_rating_popularity_stats("Ratingx", "hehe") == "Invalid index or type"
    
    def test_get_actor_movies1(self):
        ret = get_actor_movies_release_year_range("Tom Hanks", 2010, 2010)
        
        exp = pd.Series([2010], index=["Toy Story 3"])
        
        assert ret.equals(exp)
        
    def test_get_actor_movies2(self):
        ret = get_actor_movies_release_year_range("Tom Hanks", 2010)
        
        exp = pd.Series([1994, 1998, 1999, 1995, 2010, 2002], index=["Forrest Gump", "Saving Private Ryan", "The Green Mile", "Toy Story", "Toy Story 3", "Catch Me If You Can"])

        assert ret.equals(exp)
    
    def test_get_actor_movies3(self):
        ret = get_actor_movies_release_year_range("Tom Hanks", 2022, 2011)
        
        exp = pd.Series([], dtype="int64")
        
        assert ret.equals(exp)
    
    def test_get_actor_movies4(self):
        ret = get_actor_movies_release_year_range("Jürgen Prochnow", 1999)
        
        exp = pd.Series([1981], index=["The Boat"])

        assert ret.equals(exp)
    
    def test_get_actor_movies5(self):
        with pytest.raises(ValueError):
            ret = get_actor_movies_release_year_range("Tom Hanks", 2011, 2022)
            
    def test_get_actor_median_rating1(self):
        assert get_actor_median_rating("Dean-Charles Chapman") == 8.2
    
    def test_get_actor_median_rating2(self):
        assert get_actor_median_rating("Lin-Manuel Miranda") == 8.3
    
    def test_get_actor_median_rating3(self):
        with pytest.raises(ValueError):
            get_actor_median_rating("")
    
    def test_get_actor_median_rating4(self):
        with pytest.raises(TypeError):
            get_actor_median_rating(1)
    
    def test_get_actor_median_rating5(self):
        assert get_actor_median_rating("Ricky Lu") == None