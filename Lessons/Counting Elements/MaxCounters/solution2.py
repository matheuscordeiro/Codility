#!/usr/local/bin/python3

"""Task 

You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.

For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.
"""

def solution(N, A):
    counters = [0] * N
    reference_counters = [False] * N
    maximum = 0
    reference = 0
    for value in A:
      if value > N:
        reference = maximum
      else:
        if not reference_counters[value-1]:
          reference_counters[value-1] = {}
        if reference_counters[value-1].get(reference):
          counters[value-1] += 1
        else:
          counters[value-1] = reference + 1
          reference_counters[value-1][reference] = True
        if counters[value-1] > maximum:
          maximum = counters[value-1]
          reference_counters[value-1][reference] = True

    for index in range(N):
      if not reference_counters[index]:
          reference_counters[index] = {}
      if not reference_counters[index].get(reference):
        counters[index] = reference
          
    return counters