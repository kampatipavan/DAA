# DAA Lab Exercise
# Topic 4 - Dynamic Programming - Question 7

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q7 Longest substring without repeating characters
def longest_unique(s):
    last={}; left=ans=0
    for r,ch in enumerate(s):
        if ch in last and last[ch]>=left:left=last[ch]+1
        last[ch]=r; ans=max(ans,r-left+1)
    return ans
print("T4 Q7:",longest_unique("abcabcbb"),longest_unique("bbbbb"),longest_unique("pwwkew"))
