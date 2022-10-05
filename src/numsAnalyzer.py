# Run this script from the repository's root.
import numpy as np

def replaceMissingValues(x):
    '''
    Modify in place the (M, N) matrix with all the NaN turned into 0.0
    '''
    np.nan_to_num(x, copy=False, nan=0)

def countMissingValues(x, k=0):
    if type(k) != int or k >= x.ndim or k < -x.ndim:
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
    if np.any(x < 0) or np.any(x > 100):
        raise ValueError
    
    replaceMissingValues(x)
    
    med = np.median(x, axis=1) # Find the median for each semester. axis need to be 1
    med_mask = med > k # Find all the rows that has median greater than k
    filtered = x[med_mask] # Select only rows that are True
    
    # Return the number of rows that passed the filter
    return filtered.shape[0]

def curve_low_scoring_exams(x, k):
    if k > 100 or k < 0:
        raise ValueError
    if np.any(x < 0) or np.any(x > 100):
        raise ValueError
    
    replaceMissingValues(x)
    
    avg = np.mean(x, axis=1) # Find the average across the semester
    
    avg_mask = avg < k # Tells which semester requires a curve
    avg_mask = avg_mask.reshape(avg_mask.shape[0], 1) # Need to be also reshaped to be column vector
    
    # Calculate how much point need to be added
    # Need to be reshaped to column in order to be broadcasted
    curve = 100 - np.max(x, axis=1)
    curve = curve.reshape(curve.shape[0], 1)
    
    # The new matrix with curved score added to it
    x_curved = np.where(avg_mask, x + curve, x)
    
    # Get the mean of the curved grades
    x_curved_mean = np.mean(x_curved, axis=1)
    
    # Sort by the curved mean
    sorted_x = np.argsort(x_curved_mean) 
    
    # Update x_curved to the sorted one
    x_curved = x_curved[sorted_x]
    
    # Round to the tenth place
    return np.round(x_curved, 1)
