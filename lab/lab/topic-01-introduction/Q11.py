def out_paths(m,n,N,i,j):
    dp={(i,j):1}
    for _ in range(N):
        nd={}
        for (r,c),ways in dp.items():
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n: nd[(nr,nc)]=nd.get((nr,nc),0)+ways
                else: nd[(None,None)]=nd.get((None,None),0)+ways
        escaped=nd.pop((None,None),0); dp=nd
        if _==N-1: print(escaped)
out_paths(2,2,2,0,0)
