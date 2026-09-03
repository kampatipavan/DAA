# DAA Lab Exercise
# Topic 4 - Dynamic Programming - Question 4

from math import inf

# Q4 Minimum TSP tour using DP
def tsp_dp(m):
    n=len(m); dp={(1,0):0}
    for size in range(2,n+1):
        for mask in range(1<<n):
            if not(mask&1) or mask.bit_count()!=size: continue
            for last in range(1,n):
                if mask&(1<<last):
                    prev=mask^(1<<last)
                    dp[(mask,last)]=min((dp.get((prev,p),inf)+m[p][last] for p in range(n) if prev&(1<<p)),default=inf)
    full=(1<<n)-1
    return min(dp[(full,j)]+m[j][0] for j in range(1,n))
print("T4 Q4:",tsp_dp([[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]))
print("T4 Q4:",tsp_dp([[0,10,10,10],[10,0,10,10],[10,10,0,10],[10,10,10,0]]))
print("T4 Q4:",tsp_dp([[0,1,2,3],[1,0,4,5],[2,4,0,6],[3,5,6,0]]))
