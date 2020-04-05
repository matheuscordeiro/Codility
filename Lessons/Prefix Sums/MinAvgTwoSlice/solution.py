#!/usr/local/bin/python3

"""Task

A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). 
The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. 
To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

contains the following example slices:

    slice (1, 2), whose average is (2 + 2) / 2 = 2;
    slice (3, 4), whose average is (5 + 1) / 2 = 3;
    slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of a slice whose average is minimal.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. 
If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.
"""

def solution(A):
    arr = prefix_sum(A)
    size_A = len(arr)
    position = -1
    minimal = 100001
    for i in range(2, size_A):
        average = (arr[i] - arr[i-2])/2
        import pdb
        pdb.set_trace()
        if average < minimal:
            minimal = average
            position = i - 1
            
        if (i + 2) < size_A:
            average = (arr[i+2] - arr[i-2])/3    
            if average < minimal:
                minimal = average
                position = i - 1
        
    return position

        