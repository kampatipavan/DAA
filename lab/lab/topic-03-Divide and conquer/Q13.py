from itertools import combinations
def subset_closest(a,target):
    best=(float("inf"),[])
    for r in range(len(a)+1):
        for s in combinations(a,r):
            d=abs(sum(s)-target)
            if d<best[0]:best=(d,list(s))
    return best
print(subset_closest([45,34,4,12,5,2],42))
print(subset_closest([1,3,2,7,4,6],10))
print("Meet-in-the-middle reduces exhaustive subset search to about O(2^(n/2)) time.")
