#!/usr/local/bin/python3

def solution(S):
    stack = []
    for i in S:
        if i == '(':
            stack.append(i)
        elif stack:
            stack.pop()
        else:
            return 0
            
    if stack:
        return 0
    else:
        return 1