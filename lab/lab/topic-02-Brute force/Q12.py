from itertools import permutations
from math import hypot
def tsp(cities):
    start=cities[0]; best=(float("inf"),None)
    for p in permutations(cities[1:]):
        path=(start,)+p+(start,)
        d=sum(hypot(a[0]-b[0],a[1]-b[1]) for a,b in zip(path,path[1:]))
        if d<best[0]: best=(d,path)
    return best
for cities in [[(1,2),(4,5),(7,1),(3,6)],[(2,4),(8,1),(1,7),(6,3),(5,9)]]:
    d,p=tsp(cities); print("Shortest Distance:",d); print("Shortest Path:",p)
