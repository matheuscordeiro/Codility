#!/usr/local/bin/python3

"""Task 

A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

    def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.
"""

def solution(A):
    arr = sorted(A)
    print(arr)
    for index, value in enumerate(arr):
        if value != index + 1:
            return 0
    return 1    
