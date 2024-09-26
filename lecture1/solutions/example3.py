"""
Part 2, Lecture 1, Example 3

Solve a two-period optimal bun-eating problem using NumPy.
"""

from example2 import utility_total
import numpy as np


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
    # Candidate consumption levels for day 2
    c2_cand = buns - c1_cand

    # Evaluate utility for all candidate consumption levels
    utils = utility_total(c1_cand, c2_cand)
    
    # Find consumption choice that maximizes utility
    imax = np.argmax(utils)
    umax = utils[imax]

    c1_opt = c1_cand[imax]
    c2_opt = c2_cand[imax]

    print(f'Optimal consumption choice: c1={c1_opt}, c2={c2_opt}')
    print(f'Maximized utility: {umax}')


if __name__ == '__main__':
    main()