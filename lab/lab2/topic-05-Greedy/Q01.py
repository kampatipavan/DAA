# DAA Lab Exercise
# Topic 5 - Greedy - Question 1

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q1
def max_coins(p):
    p=sorted(p);ans=0;r=len(p)-1
    for _ in range(len(p)//3):r-=1;ans+=p[r];r-=1
    return ans
print("T5 Q1:",max_coins([2,4,1,2,7,8]),max_coins([2,4,5]))
