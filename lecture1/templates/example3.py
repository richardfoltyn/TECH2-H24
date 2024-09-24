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

    # Evaluate utility for candidate values and find maximum
    # ADD YOUR IMPLEMENTATION HERE
    

if __name__ == '__main__':
    main()