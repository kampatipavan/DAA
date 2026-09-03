# DAA Lab Exercise
# Topic 4 - Dynamic Programming - Question 17

from collections import deque

# Q17 Cat and Mouse Game
def cat_mouse(graph):
    n=len(graph); color=[[[0]*3 for _ in range(n)] for _ in range(n)]
    deg=[[[0]*3 for _ in range(n)] for _ in range(n)]
    q=[]
    from collections import deque
    q=deque()
    for c in range(n):
        for t in range(3):
            color[0][c][t]=1;q.append((0,c,t,1))
    for m in range(1,n):
        for t in range(3):
            color[m][m][t]=2;q.append((m,m,t,2))
    for m in range(n):
        for c in range(1,n):
            deg[m][c][0]=len(graph[m])
            deg[m][c][1]=sum(v!=0 for v in graph[c])
    while q:
        m,c,t,res=q.popleft();pt=1-t
        prev=[(pm,c,pt) for pm in graph[m]] if pt==0 else [(m,pc,pt) for pc in graph[c] if pc!=0]
        for pm,pc,turn in prev:
            if color[pm][pc][turn]:continue
            if (turn==0 and res==1) or (turn==1 and res==2):
                color[pm][pc][turn]=res;q.append((pm,pc,turn,res))
            else:
                deg[pm][pc][turn]-=1
                if deg[pm][pc][turn]==0:color[pm][pc][turn]=res;q.append((pm,pc,turn,res))
    return color[1][2][0]
print("T4 Q17:",cat_mouse([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]))
print("T4 Q17:",cat_mouse([[1,3],[0],[3],[0,2]]))
