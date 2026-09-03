def minmax(a,l,r):
    if l==r:return a[l],a[l]
    m=(l+r)//2; a1,b1=minmax(a,l,m); a2,b2=minmax(a,m+1,r)
    return min(a1,a2),max(b1,b2)
a=[2,4,6,8,10,12,14,18]; print("Min =",minmax(a,0,len(a)-1)[0],"Max =",minmax(a,0,len(a)-1)[1])
