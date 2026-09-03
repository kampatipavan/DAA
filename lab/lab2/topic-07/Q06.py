# DAA Lab Exercise
# Topic 7 - Tractability and Approximation - Question 6

from itertools import combinations

# Q6 Maximum Cut
def cut(A,E):return sum(w for u,v,w in E if (u in A)!=(v in A))
def maxcut(V,E):
    best=(-1,None)
    for mask in range(1<<(len(V)-1)):
        A={V[0]}|{V[i+1] for i in range(len(V)-1) if mask>>i&1}
        w=cut(A,E)
        if w>best[0]:best=(w,A)
    return best
print("T7 Q6:",maxcut([1,2,3,4],[(1,2,2),(1,3,1),(2,3,3),(2,4,4),(3,4,2)]))
