#!/usr/local/bin/python3

"""Task 
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

	0 represents a car traveling east,
	1 represents a car traveling west.

The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

"""

def solution(A):
    tam = len(A)
    arr = [0] * (tam + 1)
    for index in range(tam+1):
        arr[index] = {}
        if index == 0:
            arr[index][0] = arr[index]['pairs'] = 0
            continue

        value = A[index-1]        
        if value == 0:
            arr[index][0] = arr[index-1][0] + 1
            arr[index]['pairs'] = arr[index-1]['pairs']
        else:
            arr[index][0] = arr[index-1][0]
            arr[index]['pairs'] = arr[index-1]['pairs'] + arr[index][0]
            
    
    result = arr[tam]['pairs']
    if result > 1000000000:
        result = -1
    return result
