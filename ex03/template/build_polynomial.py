# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data
    # ***************************************************
    phi_xn = np.zeros((x.shape[0], degree))
    for i in range(phi_xn.shape[0]):
        phi_xn[i] = [x[i]**j for j in range(degree)]
    return phi_xn
