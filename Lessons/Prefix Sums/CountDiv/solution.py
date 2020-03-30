#!/usr/local/bin/python3

"""Task 

Write a function:

    class Solution { public int solution(int A, int B, int K); }

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

"""

def solution(A, B, K):
    count = 0
    for value in range(A, B+1):
        if value % K == 0:
            return 1 + int((B-value) / K)

    return count

print(solution(0,14,2))
