# DAA Lab Exercise
# Topic 4 - Dynamic Programming - Question 2

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q2 Two Assembly Lines
def assembly(a1,a2,t1,t2,e1,e2,x1,x2):
    f1=[e1+a1[0]]; f2=[e2+a2[0]]
    for i in range(1,len(a1)):
        f1.append(min(f1[-1]+a1[i],f2[-1]+t2[i-1]+a1[i]))
        f2.append(min(f2[-1]+a2[i],f1[-2]+t1[i-1]+a2[i]))
    return min(f1[-1]+x1,f2[-1]+x2)
print("T4 Q2:",assembly([7,9,3,4,8,4],[8,5,6,4,5,7],[2,3,1,3,4],[2,1,2,2,1],2,4,3,2))
