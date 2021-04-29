import math

def create_peaks(A):
    peaks = [False] * len(A)
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] > A[i+1]:
            peaks[i] = True

    return peaks

def create_next_peak(A):
    peaks = create_peaks(A)
    next_peaks = [-1] * len(peaks)
    for i in range(len(peaks)-2, -1, -1):
        if peaks[i]:
            next_peaks[i] = i
        else:
            next_peaks[i] = next_peaks[i+1]

    return next_peaks

def solution(A):
    N = len(A)
    next_peaks = create_next_peak(A)
    i = 1
    result = 0
    max_flags = int(math.sqrt(N)) + 1
    while i <= max_flags:  # manage flags
        pos = 0
        num = 0
        while pos < N and num < i:  # manage positions
            pos = next_peaks[pos]
            if pos == -1:
                break
            
            num += 1
            pos += i
        
        result = max(result, num)
        i += 1
    
    return result

if __name__ == "__main__":
    array = [1,5,3,4,5,4,1,2,3,4,6,2]
    # array = [1,2,3,2,2,3,2,2,2,2,10,2,2,2,3,2,3,2] # [2,5,10,14,16]
    print(solution(array))