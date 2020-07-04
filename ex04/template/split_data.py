# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np


def split_data(x, y, ratio, seed=1):
    """
    split the dataset based on the split ratio. If ratio is 0.8 
    you will have 80% of your data set dedicated to training 
    and the rest dedicated to testing
    """
    # set seed
    np.random.seed(seed)
    # ***************************************************
    # INSERT YOUR CODE HERE
    # split the data based on the given ratio: TODO
    # ***************************************************
    idx = np.random.permutation(x.shape[0])
    cut = int(np.floor(ratio * x.shape[0]))
    idx_tr = idx[:cut]
    idx_te = idx[cut:]

    x_train, y_train = x[idx_tr], y[idx_tr]
    x_test, y_test = x[idx_te], y[idx_te]
    
    return (x_train, y_train, x_test, y_test)
