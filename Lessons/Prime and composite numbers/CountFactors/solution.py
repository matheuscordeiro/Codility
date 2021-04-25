import math

def solution(N):
    limit = int(math.sqrt(N))
    count = 0
    register = {}
    for i in range(1, limit+2):
        if N % i == 0:
            if not register.get(i):
                count += 1
                register[i] = True
                
            value = int(N/i)
            if not register.get(value):
                count += 1
                register[value] = True

    return count