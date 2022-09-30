# Run this script from the repository's root.
import numpy as np

def replaceMissingValues(x):
    '''
    Modify in place the (M, N) matrix with all the NaN turned into 0.0
    '''
    np.nan_to_num(x, copy=False, nan=0)

def countMissingValues(x, k=0):
    if k >= x.ndim or k < -x.ndim:
        raise ValueError
    
    A = np.isnan(x) # boolean mask on nan values. True if it is nan, False if it isn't
    return A.sum(axis=k) # Return basically the number of nan on the specified k axis

def exams_with_median_gt_K(x, k):
    '''
    Row represent semester, column represent each student's score. (M, N), dtype is float
    Test score is between [0.0, 100.0], NaN for student didn't take test
    NaN is treated as 0.0
    '''
    if type(k) != int:
        raise TypeError
    if k > 100 or k < 0:
        raise ValueError
    if np.any(x < 0):
        raise ValueError
    
    replaceMissingValues(x)
    
    med = np.median(x, axis=1) # Find the median for each semester. axis need to be 1
    med_mask = med > k # Find all the rows that has median greater than k
    filtered = x[med_mask] # Select only rows that are True
    
    # Return the number of rows that passed the filter
    return filtered.shape[0]
        

def curve_low_scoring_exams(x, k):
    pass
