"""
Part 2, Lecture 1, Example 2

Solve a two-period optimal bun-eating problem using only built-in Python 
functions.
"""

import numpy as np
from example1 import argmax

def utility(c):
    """
    Return per-day utility of consumption c buns.

    Parameters
    ----------
    c: float
        Amount of buns consumed

    Returns
    -------
    u : float 
        Per-day utility derived from consumption
    """

    u = - ((c/50.0 - 3/2))**2.0 + 2

    return u

def utility_total(c1, c2):
    """
    Return total utility of consuming c1 today and c2 tomorrow.

    Parameters
    ----------
    c1: float
        Amount of buns consumed on day 1
    c2: float 
        Amount of buns consumed on day 2
    
    Returns
    -------
    u : float 
        Total utility derived from consumption
    """

    u1 = utility(c1)
    u2 = utility(c2)

    u = u1 + u2

    return u


def main():
    """
    Find the optimal number of buns to consume on each day.
    """

    # Number of buns received
    buns = 100
    # Grid size to evaluate optimal bun consumption
    N = 101

    # Candidate consumption levels for day 1
    c1_cand = np.linspace(0.0, buns, N)

    utils = []
    for c1 in c1_cand:
        # Recover number of buns eaten on day 2
        c2 = buns - c1
        u = utility_total(c1, c2)
        utils.append(u)

    # Find consumption choice that maximizes utility
    imax, umax = argmax(utils)

    c1_opt = c1_cand[imax]
    c2_opt = buns - c1_opt

    print(f'Optimal consumption choice: c1={c1_opt}, c2={c2_opt}')
    print(f'Maximized utility: {umax}')


if __name__ == '__main__':
    main()