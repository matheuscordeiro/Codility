#!/usr/bin/pthon3

# Time complexity: O(N)

def solution(A):
    count = {}
    size_A = len(A)
    leader = None
    for i, a in enumerate(A):
        count[a] = count.get(a, 0) + 1
        if count[a] > size_A // 2:
            leader = a
            
    
    equi_leader = 0
    before = 0
    for i in range(size_A):
        if A[i] == leader:
            before += 1

        if (before > (i + 1) // 2) and ((count[leader] - before) > (size_A - i - 1) // 2):
            equi_leader += 1
    
    return equi_leader
