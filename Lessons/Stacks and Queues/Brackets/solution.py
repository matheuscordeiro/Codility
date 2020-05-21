#!/usr/local/bin/python3


def solution(S):
    characters = {'{': '}', '(': ')', '[': ']'}
    stack = []
    position = -1
    for char in S:
        if characters.get(char):
            stack.append(char)
            position += 1
        elif not stack or characters[stack[position]] != char:
            return 0
        else:
            stack.pop()
            position -= 1
        
    if stack:
        return 0
    else:
        return 1

