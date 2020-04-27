#!/local/usr/bin/python3


def solution(A):
    count = 0
    distincts = {}
    for value in A:
        if not distincts.get(value):
            distincts[value] = True
            count += 1
    
    return count
