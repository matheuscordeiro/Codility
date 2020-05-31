#!/usr/bin/pthon3

BLACKLYM6

# O(N * log N)

def solution(A):
	size_A = len(A)
	if not size_A:
		return -1
	sort_A = sorted(A)
	count = 0
	dominator = sort_A[size_A // 2]
	index_dominator = -1
	for i,a in enumerate(A):
		if a == dominator:
			count += 1
			index_dominator = i

	if count > size_A // 2:
		return index_dominator
	else:
		return -1
