#!/usr/local/bin/python3

"""Task 

A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. 
Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. 
You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. 
There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. 
The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.

Write a function:
	
	def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, 
returns an array consisting of M integers specifying the consecutive answers to all queries."""

def prefix_dna(S):
	arr = [0] * (len(S) + 1)
	for index, value in enumerate(arr):
		arr[index] = {}
		if index == 0:
			arr[index]['A'] = arr[index]['C'] = arr[index]['G'] = arr[index]['T'] = 0
			continue
		
		arr[index]['A'] = arr[index-1]['A'] + (1 if S[index-1] == 'A' else 0)
		arr[index]['C'] = arr[index-1]['C'] + (1 if S[index-1] == 'C' else 0)
		arr[index]['G'] = arr[index-1]['G'] + (1 if S[index-1] == 'G' else 0)
		arr[index]['T'] = arr[index-1]['T'] + (1 if S[index-1] == 'T' else 0)
	return arr
	

def solution(S, P, Q):
	nucleotides = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
	arr = prefix_dna(S)
	M = len(P)
	result = []
	for index in range(M):
		value_Q = arr[Q[index]+1]
		value_P = arr[P[index]]
		if value_Q['A'] - value_P['A'] > 0:
			result.append(nucleotides['A'])
		elif value_Q['C'] - value_P['C'] > 0:
			result.append(nucleotides['C'])
		elif value_Q['G'] - value_P['G'] > 0:
			result.append(nucleotides['G'])
		elif value_Q['T'] - value_P['T'] > 0:
			result.append(nucleotides['T'])
	return result

