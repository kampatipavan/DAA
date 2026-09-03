# DAA Lab Exercise
# Topic 6 - Backtracking - Question 5


# Q5 Target Sum
def target_sum(a,t):
    d={0:1}
    for x in a:
        nd={}
        for s,c in d.items():nd[s+x]=nd.get(s+x,0)+c;nd[s-x]=nd.get(s-x,0)+c
        d=nd
    return d.get(t,0)
print("T6 Q5:",target_sum([1,1,1,1,1],3),target_sum([1],1))
