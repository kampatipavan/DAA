# DAA Lab Exercise
# Topic 5 - Greedy - Question 10

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q9/Q10
def greedy_weight(w,c):
    total=0
    for x in sorted(w,reverse=True):
        if total+x<=c:total+=x
    return total
def containers(w,c):
    n=0;cur=0
    for x in w:
        if cur+x<=c:cur+=x
        else:n+=1;cur=x
    return n+(bool(w))
print("T5 Q9:",greedy_weight([10,20,30,40,50],60),greedy_weight([5,10,15,20,25,30],50))
print("T5 Q10:",containers([5,10,15,20,25,30,35],50),containers([10,20,30,40,50,60,70,80],100))
