"""
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

    # ADD YOUR IMPLEMENTATION HERE


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

    # ADD YOUR IMPLEMENTATION HERE


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

    # Evaluate utility for candidate values and find maximum
    # ADD YOUR IMPLEMENTATION HERE




if __name__ == '__main__':
    main()