# sys_solve.py
# solves systems of linear equations
# usage: run sys_solve.py
#        follow prompts. Use spaces between values
#
#! /usr/bin/env python3

import numpy as np

size = int(input("Input the number of equations:  "))

# create arrays of zeroes
A = np.zeros([size, size])
B = np.zeros([1, size])

# set rows from user input
for row in range(size):
    A[row] = [int(x) for x in
              input(f"input row {row} equation coefficeints:  ").split(" ")]
B = [int(x) for x in input("input constants vector:  ").split(" ")]


solution = np.linalg.solve(A, B)
print(f"solution = {solution}")
