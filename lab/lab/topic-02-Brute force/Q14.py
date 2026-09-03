from itertools import combinations
def knapsack(weights,values,cap):
    best=(0,[])
    n=len(weights)
    for r in range(n+1):
        for s in combinations(range(n),r):
            if sum(weights[i] for i in s)<=cap:
                v=sum(values[i] for i in s)
                if v>best[0]: best=(v,list(s))
    return best
print(knapsack([2,3,1],[4,5,3],4))
print(knapsack([1,2,3,4],[2,4,6,3],6))
