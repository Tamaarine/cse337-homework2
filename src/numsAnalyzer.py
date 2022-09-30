# Run this script from the repository's root.
import numpy as np

def replaceMissingValues(x):
    pass

def countMissingValues(x, k=0):
    if k >= x.ndim or k < -x.ndim:
        raise ValueError
    
    A = np.isnan(x) # boolean mask on nan values. True if it is nan, False if it isn't
    return A.sum(axis=k) # Return basically the number of nan on the specified k axis

def exams_with_median_gt_K(x, k):
    pass

def curve_low_scoring_exams(x, k):
    pass
