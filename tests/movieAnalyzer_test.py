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