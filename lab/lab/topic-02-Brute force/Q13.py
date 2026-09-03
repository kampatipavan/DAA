from itertools import permutations
def assignment(cost):
    n=len(cost); best=(float("inf"),None)
    for p in permutations(range(n)):
        c=sum(cost[i][p[i]] for i in range(n))
        if c<best[0]: best=(c,p)
    return best
for cost in [[[3,10,7],[8,5,12],[4,6,9]],[[15,9,4],[8,7,18],[6,12,11]]]:
    c,p=assignment(cost); print("Assignment:",[(i+1,p[i]+1) for i in range(len(p))],"Total Cost:",c)
