#!/usr/local/bin/python3

MAXIMUM = 10E6

def solution(A):
	size_A = len(A)
	opened = [0] * size_A
	closed = [0] * size_A
	for i in range(size_A):
		opened[i] = i - A[i]
		closed[i] = i + A[i]


	opened = sorted(opened)
	closed = sorted(closed)
	count = actived = 0
	i = j = 0
	while i < size_A and j < size_A:
		if opened[i] <= closed[j]:
			count += actived
			actived += 1
			i += 1
		else:
			actived -= 1
			j += 1

		if count > MAXIMUM:
			return -1

	return count
