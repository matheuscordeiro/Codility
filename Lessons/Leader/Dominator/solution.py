#!/usr/bin/sh

# Time complexity: O(n)

def solution(A):
    count = {}
    size_A = len(A)
    for i, a in enumerate(A):
        count[a] = count.get(a, 0) + 1
        if count[a] > size_A // 2:
            return i
    
    return -1
