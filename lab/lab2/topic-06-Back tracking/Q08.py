# DAA Lab Exercise
# Topic 6 - Backtracking - Question 8


# Combination Sum II helper
def comb_sum(a,t,once=False):
    a=sorted(a);res=[]
    def bt(start,rem,path):
        if rem==0:res.append(path[:]);return
        for i in range(start,len(a)):
            if i>start and once and a[i]==a[i-1]:continue
            if a[i]>rem:break
            path.append(a[i]);bt(i+1 if once else i,rem-a[i],path);path.pop()
    bt(0,t,[]);return res
print("T6 Q7:",comb_sum([2,3,6,7],7))
print("T6 Q8:",comb_sum([10,1,2,7,6,1,5],8,True))
