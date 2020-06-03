#!/usr/bin/python3


def solution(A):
    max_ending = 0
    max_slice = -1000001
    for a in A:
        max_slice = max(max_slice, max_ending + a)
        max_ending = max(0, max_ending + a)

    return max_slice
    