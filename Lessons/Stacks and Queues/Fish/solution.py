#!/usr/local/bin/python3


def solution(A, B):
    size_A = len(A)
    stack_down = []
    head = 0
    count = 0
    for i in range(size_A):
        count += 1
        if B[i]:
            stack_down.append(A[i])
            head += 1
        else:
            while(stack_down):
                count -= 1
                if stack_down[head-1] > A[i]:
                    break
                else:
                    stack_down.pop()
                    head -= 1
            
    return count