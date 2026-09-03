# DAA Lab Exercise
# Topic 5 - Greedy - Question 2

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q2
def patches(coins,target):
    coins=sorted(coins);reach=1;i=ans=0
    while reach<=target:
        if i<len(coins) and coins[i]<=reach:reach+=coins[i];i+=1
        else:reach*=2;ans+=1
    return ans
print("T5 Q2:",patches([1,4,10],19),patches([1,4,10,5,7,19],19))
