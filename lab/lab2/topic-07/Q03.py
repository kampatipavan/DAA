# DAA Lab Exercise
# Topic 7 - Tractability and Approximation - Question 3

from itertools import combinations

# Q3 Vertex Cover
def is_cover(c,e):return all(u in c or v in c for u,v in e)
def exact_cover(V,E):
    for r in range(len(V)+1):
        for c in combinations(V,r):
            if is_cover(set(c),E):return set(c)
def approx_cover(E):
    c=set()
    for u,v in E:
        if u not in c and v not in c:c|={u,v}
    return c
E=[(1,2),(1,3),(2,3),(3,4),(4,5)]
print("T7 Q3:",approx_cover(E),exact_cover([1,2,3,4,5],E))
