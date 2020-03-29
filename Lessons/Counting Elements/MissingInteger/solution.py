#!/usr/local/bin/python3

"""Task 

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
"""

def solution(A):
    minimum = 1
    arr = sorted(A)
    for value in arr:
        if value == minimum:
            minimum += 1
        elif value < minimum:
            continue
        else:
            return minimum

    return minimum

print(solution([0,-3,-2]))
