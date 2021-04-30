def _peaks(A):
    peaks = [False] * len(A)
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] > A[i+1]:
            peaks[i] = True

    return peaks


def create_peaks(A):
    peaks = _peaks(A)
    count = 0
    for key, value in enumerate(peaks):
        if value:
            count += 1
        
        peaks[key] = count

    return peaks, count


def solution(A):
    peaks, limit = create_peaks(A)
    N = len(A)
    for i in range(limit, 0, -1):
        if N % i == 0:
            walk = (N // i)
            pos = walk - 1
            before = blocks = 0
            while pos < N:
                if peaks[pos] - before >= 1:
                    before = peaks[pos]
                    pos += walk
                    blocks += 1
                else:
                    break
            
            if blocks == i:
                return blocks

    return 0


if __name__ == "__main__":
    array = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
    print(solution(array))