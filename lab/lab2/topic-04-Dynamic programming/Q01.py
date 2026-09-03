# DAA Lab Exercise
# Topic 4 - Dynamic Programming - Question 1

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q1 Dice Throw
def dice_ways(sides, dice, target):
    dp=[[0]*(target+1) for _ in range(dice+1)]
    dp[0][0]=1
    for d in range(1,dice+1):
        for s in range(1,target+1):
            for face in range(1,sides+1):
                if s>=face: dp[d][s]+=dp[d-1][s-face]
    return dp[dice][target]
print("T4 Q1:",dice_ways(6,2,7),dice_ways(4,3,10))
