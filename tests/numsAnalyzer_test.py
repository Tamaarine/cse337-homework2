from numpy import array_equal
import pytest
import sys, os
sys.path.insert(1, os.getcwd())
from src.numsAnalyzer import np, countMissingValues, curve_low_scoring_exams, exams_with_median_gt_K, replaceMissingValues

class TestNumsAnalyzer:
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
    
    def test_replace_missing1(self):
        size = (5, 3)
        np.random.seed(6969)
        
        num_true = int(np.prod(size) * 0.4)
        
        mask = np.zeros(np.prod(size), dtype=bool)
        mask[:num_true] = True
        np.random.shuffle(mask)
        mask = mask.reshape(size)
        
        x = np.random.randint(100, size=size)
        x = x.astype(dtype="float64")
        x[mask] = np.NaN
        
        exp = np.array([[0, 92, 0], [0, 45, 39], [96, 78, 0], [21, 37, 0], [0, 79, 51]], dtype="float64")
        
        replaceMissingValues(x)  
        
        assert np.array_equal(x, exp)
    
    def test_exams_median_get1(self):
        x = np.array([100.0, 87.3, 94.5, 99.0, 78.4,
                    82.6, 71.3, 99.9, np.nan, 48.0,
                    92.6, np.nan, 43.5, np.nan, 80.0,
                    97.0, np.nan, 98.5, np.nan, 65.3])
        
        x = x.reshape((4, 5))
        
        assert exams_with_median_gt_K(x, 70) == 2
    def test_exams_median_get2(self):
        size = (5, 10)
        np.random.seed(120120)
                
        x = np.random.uniform(0, 100, size=(np.prod(size)))
        np.random.shuffle(x)
        x = x.reshape(size)
        
        assert exams_with_median_gt_K(x, 50) == 2
    
    def test_exams_median_get3(self):
        size = (8, 10)
        np.random.seed(5633)
                
        x = np.random.uniform(0, 100, size=(np.prod(size)))
        np.random.shuffle(x)
        x = x.reshape(size)
        
        assert exams_with_median_gt_K(x, 50) == 6
    
    def test_exams_median_get4(self):
        with pytest.raises(TypeError):
            size = (8, 10)
            np.random.seed(5633)
                    
            x = np.random.uniform(0, 100, size=(np.prod(size)))
            np.random.shuffle(x)
            x = x.reshape(size)
            
            exams_with_median_gt_K(x, "hello world")
    
    def test_exams_median_get5(self):
        with pytest.raises(TypeError):
            size = (8, 10)
            np.random.seed(5633)
                    
            x = np.random.uniform(0, 100, size=(np.prod(size)))
            np.random.shuffle(x)
            x = x.reshape(size)
            
            exams_with_median_gt_K(x, True)
    
    def test_exams_median_get6(self):
        with pytest.raises(ValueError):
            size = (8, 10)
            np.random.seed(5633)
                    
            x = np.random.uniform(0, 100, size=(np.prod(size)))
            np.random.shuffle(x)
            x = x.reshape(size)
            
            exams_with_median_gt_K(x, -4)
    
    def test_exams_median_get7(self):
        with pytest.raises(ValueError):
            size = (8, 10)
            np.random.seed(5633)
                    
            x = np.random.uniform(0, 100, size=(np.prod(size)))
            np.random.shuffle(x)
            x = x.reshape(size)
            
            exams_with_median_gt_K(x, 104)
    
    def test_exams_median_get8(self):
        with pytest.raises(ValueError):
            size = (8, 10)
            np.random.seed(5633)
                    
            x = np.random.uniform(0, 100, size=(np.prod(size)))
            np.random.shuffle(x)
            x = x.reshape(size)
            x[0][0] = -3
            
            exams_with_median_gt_K(x, 30)

    def test_exams_median_get9(self):
        with pytest.raises(ValueError):
            size = (8, 10)
            np.random.seed(5633)
                    
            x = np.random.uniform(0, 100, size=(np.prod(size)))
            np.random.shuffle(x)
            x = x.reshape(size)
            x[0][0] = 102
            
            exams_with_median_gt_K(x, 30)
            
    def test_curve_low_scoring_exams1(self):
        size = (4, 4)
        np.random.seed(7878)
        
        x = np.random.uniform(0, 100, size=(np.prod(size)))
        np.random.shuffle(x)
        x = x.reshape(size)
        
        y = curve_low_scoring_exams(x, 60)
        
        exp = np.array([[4.9, 100, 19, 87.3], [45.6, 94.3, 17.8, 98.3], [60.4, 80, 52.8, 98.8], [100, 89.4, 90.4, 90.1]])

        assert np.array_equal(y, exp)
    
    def test_curve_low_scoring_exams2(self):
        size = (5, 4)
        np.random.seed(676)
        
        x = np.random.uniform(0, 100, size=(np.prod(size)))
        np.random.shuffle(x)
        x = x.reshape(size)
        
        y = curve_low_scoring_exams(x, 60)
        
        exp = np.array([[61.7, 50.9, 41.6, 93.1], [100, 56,60.7, 48.2], [ 99.7, 90.3, 14.9, 64.7], [84.5, 73.5, 60.4, 60], [36.2, 99.3, 92.9, 56.2]])

        assert np.array_equal(y, exp)
    
    def test_curve_low_scoring_exams3(self):
        with pytest.raises(TypeError):
            size = (5, 4)
            np.random.seed(676)
            
            x = np.random.uniform(0, 100, size=(np.prod(size)))
            np.random.shuffle(x)
            x = x.reshape(size)
            
            y = curve_low_scoring_exams(x, "hehe xd")
    
    def test_curve_low_scoring_exams4(self):
        with pytest.raises(ValueError):
            size = (5, 4)
            np.random.seed(676)
            
            x = np.random.uniform(0, 100, size=(np.prod(size)))
            np.random.shuffle(x)
            x = x.reshape(size)
            
            y = curve_low_scoring_exams(x, 104)
    
    def test_curve_low_scoring_exams5(self):
        with pytest.raises(ValueError):
            size = (5, 4)
            np.random.seed(676)
            
            x = np.random.uniform(0, 100, size=(np.prod(size)))
            np.random.shuffle(x)
            x = x.reshape(size)
            
            y = curve_low_scoring_exams(x, -39)
    
    def test_curve_low_scoring_exams6(self):
        with pytest.raises(ValueError):
            size = (5, 4)
            np.random.seed(676)
            
            x = np.random.uniform(0, 100, size=(np.prod(size)))
            np.random.shuffle(x)
            x = x.reshape(size)
            x[0][0] = -3
            
            y = curve_low_scoring_exams(x, 50)
    
    def test_curve_low_scoring_exams7(self):
        with pytest.raises(ValueError):
            size = (5, 4)
            np.random.seed(676)
            
            x = np.random.uniform(0, 100, size=(np.prod(size)))
            np.random.shuffle(x)
            x = x.reshape(size)
            x[0][0] = 104
            
            y = curve_low_scoring_exams(x, 50)