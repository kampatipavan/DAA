from itertools import combinations
def dist(a,b): return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
pts=[(10,0),(11,5),(5,3),(9,3.5),(15,3),(12.5,7),(6,6.5),(7.5,4.5)]
best=(float("inf"),None)
for a,b in combinations(pts,2):
    d=dist(a,b)
    if d<best[0]: best=(d,(a,b))
print("Closest pair:",best[1],"Distance:",best[0])
print("Brute-force pair search: O(n^2)")
