# DAA Lab Exercise
# Topic 4 - Dynamic Programming - Question 6

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q6 Longest Palindromic Substring
def longest_pal(s):
    if len(s)<2:return s
    best=s[0]
    for c in range(len(s)):
        for l,r in [(c,c),(c,c+1)]:
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>len(best):best=s[l:r+1]
                l-=1;r+=1
    return best
print("T4 Q6:",longest_pal("babad"),longest_pal("cbbd"))
