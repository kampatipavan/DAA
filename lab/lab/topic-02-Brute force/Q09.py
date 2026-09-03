from math import hypot
pts=[(1,2),(4,5),(7,8),(3,1)]
best=(float("inf"),None)
for i in range(len(pts)):
    for j in range(i+1,len(pts)):
        d=hypot(pts[i][0]-pts[j][0],pts[i][1]-pts[j][1])
        if d<best[0]: best=(d,(pts[i],pts[j]))
print("Closest pair:",best[1],"Minimum distance:",best[0])
print("Time Complexity: O(n^2)")
