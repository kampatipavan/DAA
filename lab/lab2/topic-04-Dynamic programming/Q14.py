# DAA Lab Exercise
# Topic 4 - Dynamic Programming - Question 14

from math import inf

def floyd(a):
    d=[r[:] for r in a]; n=len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n): d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d

def city(n,edges,threshold):
    d=[[inf]*n for _ in range(n)]
    for i in range(n): d[i][i]=0
    for u,v,w in edges: d[u][v]=d[v][u]=min(d[u][v],w)
    d=floyd(d)
    counts=[sum(d[i][j]<=threshold for j in range(n) if i!=j) for i in range(n)]
    return max(i for i,c in enumerate(counts) if c==min(counts))

# Q12/Q13/Q14 Floyd-Warshall
def floyd(a):
    d=[r[:] for r in a];n=len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d
def city(n,edges,threshold):
    d=[[inf]*n for _ in range(n)]
    for i in range(n):d[i][i]=0
    for u,v,w in edges:d[u][v]=d[v][u]=min(d[u][v],w)
    d=floyd(d); counts=[sum(d[i][j]<=threshold for j in range(n) if i!=j) for i in range(n)]
    return max(i for i,c in enumerate(counts) if c==min(counts))
print("T4 Q12:",city(4,[[0,1,3],[1,2,1],[1,3,4],[2,3,1]],4))
print("T4 Q14:",city(5,[[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]],2))
