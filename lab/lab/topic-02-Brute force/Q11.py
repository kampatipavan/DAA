def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(points):
    pts=sorted(set(points))
    if len(pts)<=1:return pts
    lo=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(pts):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0: hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]
print("Convex Hull:",hull([(1,1),(4,6),(8,1),(0,0),(3,3)]))
print("Brute-force concept: test point triples/edges; handle collinear points by retaining extreme endpoints.")
