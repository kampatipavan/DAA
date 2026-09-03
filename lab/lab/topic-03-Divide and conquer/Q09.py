import heapq
def k_closest(points,k):
    return heapq.nsmallest(k,points,key=lambda p:p[0]*p[0]+p[1]*p[1])
print(k_closest([[1,3],[-2,2],[5,8],[0,1]],2))
print(k_closest([[1,3],[-2,2]],1))
print(k_closest([[3,3],[5,-1],[-2,4]],2))
