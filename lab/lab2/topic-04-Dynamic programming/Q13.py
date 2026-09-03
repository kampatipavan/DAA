# DAA Lab Exercise
# Topic 4 - Dynamic Programming - Question 13

from math import inf

def floyd(a):
    d=[r[:] for r in a]; n=len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n): d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d

# Q13 Router failure
R=[[inf]*6 for _ in range(6)]
for i in range(6):R[i][i]=0
for u,v,w in [(0,1,1),(0,2,5),(1,2,2),(1,3,1),(2,4,3),(3,4,1),(3,5,6),(4,5,2)]:R[u][v]=R[v][u]=w
before=floyd(R);R[1][3]=R[3][1]=inf;after=floyd(R)
print("T4 Q13 A-F:",before[0][5],after[0][5])
