#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a Solid Linear Equation Solver.
"""

def solve(A, b):
    """This solves a given linear equation system.

    Ax - b = 0

    We solve for x = A^-1 * b

    :A: The coefficient matrix for A.
    :b: The result vector b.
    :returns: The solution to this equation system x as np.vector().

    EXAMPLES:
    ---------
    >>> solve([[1, 2], [3, 5]], [[10], [20]])
    matrix([[-10.],
            [ 10.]])

    >>> solve([[1, 1], [2, 4]], [[35], [94]])
    matrix([[23.],
            [12.]])
    """
    import numpy as np
    import numpy.linalg as mat

    A = np.matrix(A)
    b = np.matrix(b)

    A_inv = mat.inv(A)

    x = A_inv * b

    return x

if __name__ == "__main__":
    import doctest
    doctest.testmod()
