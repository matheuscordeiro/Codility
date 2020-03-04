#!/usr/local/bin/python3

"""Task 

An array A consisting of N different integers is given. 
The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
Your goal is to find that missing element.
"""

def solution(A):
    arr = sorted(A)
    missing = None
    value = 0
    for index, value in enumerate(arr):
    	if index + 1 != value:
    		missing = index + 1
    		break

    if not missing:
    	missing = value + 1

    return missing
