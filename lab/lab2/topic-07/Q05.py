# DAA Lab Exercise
# Topic 7 - Tractability and Approximation - Question 5

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q5 First Fit Bin Packing
def bin_pack(w,cap):
    bins=[]
    for x in w:
        for b in bins:
            if sum(b)+x<=cap:b.append(x);break
        else:bins.append([x])
    return bins
print("T7 Q5:",bin_pack([4,8,1,4,2,1],10))
