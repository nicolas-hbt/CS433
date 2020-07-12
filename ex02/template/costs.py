# -*- coding: utf-8 -*-
"""Function used to compute the loss."""

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