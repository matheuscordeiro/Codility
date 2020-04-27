#!/local/usr/bin/python3

# O(N * log(N))
def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    size_arr = len(A)
    bigger1 = A[size_arr-1]
    bigger2 = A[size_arr-2]
    bigger3 = A[size_arr-3]
    smaller1 = A[0]
    smaller2 = A[1]
    
    value_with_positive = bigger1 * bigger2 * bigger3
    value_with_negative = bigger1 * smaller1 * smaller2
    if value_with_positive > value_with_negative:
        return value_with_positive
    else:
        return value_with_negative