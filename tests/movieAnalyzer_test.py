import pytest
import sys, os
import numpy as np

sys.path.insert(1, os.getcwd())
from src.numsAnalyzer import countMissingValues
from src.movieAnalyzer import pd, get_movies_interval, get_rating_popularity_stats, get_actor_movies_release_year_range, get_actor_median_rating, get_directors_median_reviews

class TestMovieAnalyzer:
    def test_missing_count1(self):
        np.random.seed(120)
        
        size = (4, 3)
        num_true = int(np.prod(size) * 0.5)
        
        mask = np.zeros(np.prod(size), dtype=bool)
        mask[:num_true] = True
        np.random.shuffle(mask)
        mask = mask.reshape(size)
        
        x = np.random.uniform(0, 100, size=size)
        x[mask] = np.NaN
        
        assert np.array_equal(countMissingValues(x, 0), np.array([1, 3, 2]))
    
    def test_missing_count2(self):
        np.random.seed(120)
        
        size = (4, 3)
        num_true = int(np.prod(size) * 0.5)
        
        mask = np.zeros(np.prod(size), dtype=bool)
        mask[:num_true] = True
        np.random.shuffle(mask)
        mask = mask.reshape(size)
        
        x = np.random.uniform(0, 100, size=size)
        x[mask] = np.NaN

        assert np.array_equal(countMissingValues(x, 1), np.array([2, 1, 2, 1]))
    
    def test_missing_count3(self):
        np.random.seed(420)
        
        size = (10, 5)
        num_true = int(np.prod(size) * 0.5)
        
        mask = np.zeros(np.prod(size), dtype=bool)
        mask[:num_true] = True
        np.random.shuffle(mask)
        mask = mask.reshape(size)
        
        x = np.random.uniform(0, 100, size=size)
        x[mask] = np.NaN

        assert np.array_equal(countMissingValues(x, 0), np.array([4, 6, 6, 3, 6]))
        
    def test_missing_count4(self):
        np.random.seed(420)
        
        size = (10, 5)
        num_true = int(np.prod(size) * 0.5)
        
        mask = np.zeros(np.prod(size), dtype=bool)
        mask[:num_true] = True
        np.random.shuffle(mask)
        mask = mask.reshape(size)
        
        x = np.random.uniform(0, 100, size=size)
        x[mask] = np.NaN

        assert np.array_equal(countMissingValues(x, 1), np.array([2, 2, 2, 2, 2, 3, 3, 4, 3, 2]))
    
    def test_missing_count5(self):
        np.random.seed(420)
        
        size = (10, 1)
        num_true = int(np.prod(size) * 0.5)
        
        mask = np.zeros(np.prod(size), dtype=bool)
        mask[:num_true] = True
        np.random.shuffle(mask)
        mask = mask.reshape(size)
        
        x = np.random.uniform(0, 100, size=size)
        x[mask] = np.NaN
        
        print()
        print(x)

        assert np.array_equal(countMissingValues(x, 0), np.array([5]))
        
    def test_missing_count6(self):
        np.random.seed(420)
        
        size = (10, 1)
        num_true = int(np.prod(size) * 0.5)
        
        mask = np.zeros(np.prod(size), dtype=bool)
        mask[:num_true] = True
        np.random.shuffle(mask)
        mask = mask.reshape(size)
        
        x = np.random.uniform(0, 100, size=size)
        x[mask] = np.NaN
        
        print()
        print(x)

        assert np.array_equal(countMissingValues(x, 1), np.array([0, 0, 1, 1, 1, 0, 1, 0, 0, 1]))
    
    def test_missing_count7(self):
        np.random.seed(420)
        
        size = (0, 0)
        num_true = int(np.prod(size) * 0.5)
        
        mask = np.zeros(np.prod(size), dtype=bool)
        mask[:num_true] = True
        np.random.shuffle(mask)
        mask = mask.reshape(size)
        
        x = np.random.uniform(0, 100, size=size)
        x[mask] = np.NaN
        
        assert np.array_equal(countMissingValues(x, 1), np.array([]))
    
    def test_missing_count8(self):
        with pytest.raises(ValueError):
            size = (1, 20, 5)
            
            x = np.random.uniform(0, 100, size=size)
            
            countMissingValues(x, 3)
    
    def test_missing_count9(self):
        with pytest.raises(ValueError):
            size = (1, 20, 5)
            
            x = np.random.uniform(0, 100, size=size)
            
            countMissingValues(x, -4)
        
    def test_missing_count10(self):
        size = (3, 5, 3)
        np.random.seed(6969)
        
        num_true = int(np.prod(size) * 0.4)
        
        mask = np.zeros(np.prod(size), dtype=bool)
        mask[:num_true] = True
        np.random.shuffle(mask)
        mask = mask.reshape(size)
        
        x = np.random.uniform(0, 100, size=size)
        x[mask] = np.NaN
        
        exp = np.array([[1, 2, 1], [1, 1, 2], [2, 1, 1], [0, 2, 0], [2, 2, 0]])
        
        assert np.array_equal(countMissingValues(x, 0), exp)
    
    def test_missing_count11(self):
        size = (3, 5, 3)
        np.random.seed(6969)
        
        num_true = int(np.prod(size) * 0.4)
        
        mask = np.zeros(np.prod(size), dtype=bool)
        mask[:num_true] = True
        np.random.shuffle(mask)
        mask = mask.reshape(size)
        
        x = np.random.uniform(0, 100, size=size)
        x[mask] = np.NaN
        
        exp = np.array([[2, 4, 2], [2, 2, 1], [2, 2, 1]])
        
        assert np.array_equal(countMissingValues(x, 1), exp)
    
    def test_missing_count12(self):
        size = (3, 5, 3)
        np.random.seed(6969)
        
        num_true = int(np.prod(size) * 0.4)
        
        mask = np.zeros(np.prod(size), dtype=bool)
        mask[:num_true] = True
        np.random.shuffle(mask)
        mask = mask.reshape(size)
        
        x = np.random.uniform(0, 100, size=size)
        x[mask] = np.NaN
        
        exp = np.array([[2, 1, 2, 1, 2], [1, 1, 2, 0, 1], [1, 2, 0, 1, 1]])
        
        assert np.array_equal(countMissingValues(x, 2), exp)
    
    def test_missing_count13(self):
        size = (3, 5, 3)
        np.random.seed(6969)
        
        num_true = int(np.prod(size) * 0.4)
        
        mask = np.zeros(np.prod(size), dtype=bool)
        mask[:num_true] = True
        np.random.shuffle(mask)
        mask = mask.reshape(size)
        
        x = np.random.uniform(0, 100, size=size)
        x[mask] = np.NaN
        
        exp = np.array([[2, 1, 2, 1, 2], [1, 1, 2, 0, 1], [1, 2, 0, 1, 1]])
        
        assert np.array_equal(countMissingValues(x, -1), exp)
    
    def test_missing_count14(self):
        size = (3, 5, 3)
        np.random.seed(6969)
        
        num_true = int(np.prod(size) * 0.4)
        
        mask = np.zeros(np.prod(size), dtype=bool)
        mask[:num_true] = True
        np.random.shuffle(mask)
        mask = mask.reshape(size)
        
        x = np.random.uniform(0, 100, size=size)
        x[mask] = np.NaN
        
        exp = np.array([[2, 4, 2], [2, 2, 1], [2, 2, 1]])
        
        assert np.array_equal(countMissingValues(x, -2), exp)
    
    def test_missing_count15(self):
        size = (3, 5, 3)
        np.random.seed(6969)
        
        num_true = int(np.prod(size) * 0.4)
        
        mask = np.zeros(np.prod(size), dtype=bool)
        mask[:num_true] = True
        np.random.shuffle(mask)
        mask = mask.reshape(size)
        
        x = np.random.uniform(0, 100, size=size)
        x[mask] = np.NaN
        
        exp = np.array([[1, 2, 1], [1, 1, 2], [2, 1, 1], [0, 2, 0], [2, 2, 0]])
        
        assert np.array_equal(countMissingValues(x, -3), exp)