# DAA Lab Exercise
# Topic 5 - Greedy - Question 11

from itertools import combinations

class DSU:
    def __init__(self,n): self.p=list(range(n))
    def find(self,x):
        if self.p[x]!=x:self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,a,b):
        a,b=self.find(a),self.find(b)
        if a==b:return False
        self.p[b]=a;return True

# Q11/Q12 Kruskal
class DSU:
    def __init__(self,n):self.p=list(range(n))
    def find(self,x):
        if self.p[x]!=x:self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,a,b):
        a,b=self.find(a),self.find(b)
        if a==b:return False
        self.p[b]=a;return True
def kruskal(n,e):
    d=DSU(n);mst=[];tot=0
    for u,v,w in sorted(e,key=lambda x:x[2]):
        if d.union(u,v):mst.append((u,v,w));tot+=w
    return mst,tot
print("T5 Q11:",kruskal(4,[(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]))
print("T5 Q11:",kruskal(5,[(0,1,2),(0,3,6),(1,2,3),(1,3,8),(1,4,5),(2,4,7),(3,4,9)]))

def mst_unique(n,e,given):
    gw=sum(x[2] for x in given);trees=[]
    for c in combinations(e,n-1):
        d=DSU(n);ok=True;w=0
        for u,v,x in c:
            if not d.union(u,v):ok=False;break
            w+=x
        if ok and len({d.find(i) for i in range(n)})==1 and w==gw:trees.append(c)
    alt=next((list(t) for t in trees if set(t)!=set(given)),None)
    return len(trees)==1,alt
print("T5 Q12:",mst_unique(4,[(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)],[(2,3,4),(0,3,5),(0,1,10)]))

def kruskal(n,e):
    d=DSU(n);mst=[];tot=0
    for u,v,w in sorted(e,key=lambda x:x[2]):
        if d.union(u,v):mst.append((u,v,w));tot+=w
    return mst,tot
