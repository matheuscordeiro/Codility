#!/local/usr/bin/python3

def solution(A):
    A = sorted(A)
    size_A = len(A)
    for i in range(size_A-2):
        if (
            A[i] + A[i+1] > A[i+2] and
            A[i] + A[i+2] > A[i+1] and
            A[i+1] + A[i+2] > A[i]
        ):
            return 1
    
    return 0
