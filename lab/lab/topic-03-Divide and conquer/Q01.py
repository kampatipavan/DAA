def minmax(a,l,r):
    if l==r:return a[l],a[l]
    m=(l+r)//2
    mn1,mx1=minmax(a,l,m); mn2,mx2=minmax(a,m+1,r)
    return min(mn1,mn2),max(mx1,mx2)
for a in ([5,7,3,4,9,12,6,2],[1,3,5,7,9,11,13,15,17],[22,34,35,36,43,67,12,13,15,17]): print("Min, Max =",minmax(a,0,len(a)-1))
