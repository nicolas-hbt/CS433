# -*- coding: utf-8 -*-
import numpy as np
"""A function to compute the cost."""
def compute_loss(y, tx, w, loss_type='mse'):
    """Calculate the loss.

    You can calculate the loss using mse or mae.
    """
    e = y - tx.dot(w)
    if loss_type == 'mse':  
        return 1/2*np.mean(e**2)
    elif loss_type == 'mae':
        return np.mean(np.abs(e))
    else :
        print('Error in the loss function.')

def compute_mse(y, tx, w):
    """compute the loss by mse."""
    e = y - tx.dot(w)
    mse = e.dot(e) / (2 * len(e))
    return mse

