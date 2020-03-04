#!/usr/local/bin/python3

"""Task 

A small frog wants to get to the other side of the road. 
The frog is currently located at position X and wants to get to a position greater than or equal to Y. 
The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.
"""

def solution(X, Y, D):
    distance = Y - X
    jumps = distance // D
    if distance % D > 0:
	    jumps += 1
    
    return jumps
