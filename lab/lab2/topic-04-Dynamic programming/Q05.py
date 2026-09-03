# DAA Lab Exercise
# Topic 4 - Dynamic Programming - Question 5

from itertools import permutations
from math import inf

# Q5 TSP with five cities
def tsp(m):
    n=len(m); best=inf; path=None
    for p in permutations(range(1,n)):
        r=(0,)+p+(0,); c=sum(m[r[i]][r[i+1]] for i in range(n))
        if c<best: best,path=c,r
    return path,best
m5=[[0,10,15,20,25],[10,0,35,25,30],[15,35,0,30,20],[20,25,30,0,15],[25,30,20,15,0]]
print("T4 Q5:",tsp(m5))
