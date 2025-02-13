# mathtools/statistics.py

import numpy as np
from typing import List, Union, Optional

def calculate_weighted_mean(values: List[float], 
                          weights: Optional[List[float]] = None) -> float:
    """
    Calculate the weighted arithmetic mean of a list of values.

    Parameters
    ----------
    values : List[float]
        List of numerical values
    weights : List[float], optional
        List of weights corresponding to the values. 
        If None, equal weights are assumed.

    Returns
    -------
    float
        The weighted arithmetic mean

    Examples
    --------
    >>> values = [1, 2, 3, 4, 5]
    >>> weights = [0.1, 0.2, 0.4, 0.2, 0.1]
    >>> calculate_weighted_mean(values, weights)
    3.0

    Notes
    -----
    The weighted mean is calculated as:
    Σ(value * weight) / Σ(weight)
    """
    if weights is None:
        weights = [1.0] * len(values)
    
    if len(values) != len(weights):
        raise ValueError("Length of values and weights must match")
    
    return np.average(values, weights=weights)


def find_outliers(data: List[float], 
                  threshold: float = 2.0) -> List[bool]:
    """
    Detect outliers in a dataset using z-score method.

    Parameters
    ----------
    data : List[float]
        List of numerical values to check for outliers
    threshold : float, optional
        Z-score threshold for outlier detection (default is 2.0)

    Returns
    -------
    List[bool]
        Boolean mask where True indicates an outlier

    Examples
    --------
    >>> data = [1, 2, 100, 3, 4, 5]
    >>> find_outliers(data)
    [False, False, True, False, False, False]
    """
    z_scores = (np.array(data) - np.mean(data)) / np.std(data)
    return list(abs(z_scores) > threshold)