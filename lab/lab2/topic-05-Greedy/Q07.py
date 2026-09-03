# DAA Lab Exercise
# Topic 5 - Greedy - Question 7

import heapq

# Q7/Q8 Huffman
class H:
    def __init__(self,c=None,f=0,l=None,r=None):self.c,self.f,self.l,self.r=c,f,l,r
def huffman(chars,freq):
    h=[];cnt=0
    for c,f in zip(chars,freq):heapq.heappush(h,(f,cnt,H(c,f)));cnt+=1
    while len(h)>1:
        a=heapq.heappop(h)[2];b=heapq.heappop(h)[2];z=H(f=a.f+b.f,l=a,r=b);heapq.heappush(h,(z.f,cnt,z));cnt+=1
    codes={}
    def dfs(x,s):
        if x.c is not None:codes[x.c]=s or "0"
        else:dfs(x.l,s+"0");dfs(x.r,s+"1")
    dfs(h[0][2],"");return codes
def hdecode(c,f,s):
    r={v:k for k,v in huffman(c,f).items()};cur="";ans=""
    for b in s:
        cur+=b
        if cur in r:ans+=r[cur];cur=""
    return ans
print("T5 Q7:",huffman(['a','b','c','d'],[5,9,12,13]))
print("T5 Q8:",hdecode(['a','b','c','d'],[5,9,12,13],"1101100111110"))
