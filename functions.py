#########################################################
##  Implementation of HW 5 Question 1, CS160 Spring22  ##
#########################################################

# Input: array (of ints) of stone damage values, and dragon health value (int)
# Returns: integer, the minimum number of stones needed to kill the dragon
# Implemented using top-down dynamic programming

import sys
import time
import numpy
from numpy import random

def magic_stones_topdown_helper(memo, stones, health):
    if health < 0: # Case 1
        return sys.maxsize
    if health == 0: # Case 2
        return 0
    elif health in memo:
        return memo[health]
    else: # Recursion
        memo[health] = 1 + magic_stones_topdown_helper(memo, stones, health-stones[0]);
        for i in range(1, len(stones)):
            # print(memo[health], 1 + magic_stones_topdown(stones, health-stones[i]))
            if (1 + magic_stones_topdown_helper(memo, stones, health-stones[i])) < memo[health]:
                memo[health] = 1 + magic_stones_topdown_helper(memo, stones, health-stones[i])
    return memo[health]

def magic_stones_topdown(stones, health):
    # TODO: Implement
    start_time = time.time()
    memo = {}
    memo_result = magic_stones_topdown_helper(memo, stones, health)
    return memo_result
# , time.time() - start_time
# "%s seconds" % (time.time() - start_time)

# Input: array (of ints) of stone damage values, and dragon health value (int)
# Returns: integer, the minimum number of stones needed to kill the dragon
# Implemented using bottom-up dynamic programming
def magic_stones_bottomup(stones, health):
    start_time = time.time()
    if health < 0: # Case 1
        return sys.maxsize
    if health == 0: # Case 2
        return 0
    table = [0] * (health + stones[-1])
    table[0] = 0
    for i in range(-stones[-1]+1, 0):
        table[i] = sys.maxsize
    for j in range(1, health + 1):
        table[j] = 1 + table[j-stones[0]];
        for k in range(1, len(stones)):
            if (1 + table[j-stones[k]] < table[j]):
                table[j] = 1 + table[j-stones[k]]
    return table[health]

# , time.time() - start_time
    # TODO: Implement

#########################################################
##  Implementation of HW 2 Question 2, CS160 Spring22  ##
#########################################################

# Input: array of integers
# Returns: integer, the number of flips in the array
def count_flips(arr):
    start_time = time.time()
    flipped = []
    # Define the count of the loops as the length of the array
    count_loops = len(arr)
    # First, iterate the number of elements for each loop
    for i in range(2, count_loops+1):
        # At each loop, compare every two elements and do flips if necessary
        for j in reversed(range(0, i-1)):
            pre = arr[j]
            post = arr[j+1]
            if (pre > post):
                arr[j] = post
                arr[j+1] = pre
                # Append each flip to the array named "flipped"
                flipped.append([pre, post])
    return len(flipped)
# , time.time() - start_time
    # TODO: Implement