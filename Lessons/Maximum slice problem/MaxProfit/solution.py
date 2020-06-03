#!/usr/bin/pthon3


def solution(A):
    if not A:
        return 0
    
    max_profit = 0
    min_value = A[0]
    for a in A:
        max_profit = max(max_profit, a - min_value)
        min_value = min(min_value, a)
    
    return max_profit