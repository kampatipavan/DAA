# DAA Lab Exercise
# Topic 7 - Tractability and Approximation - Question 4

from itertools import combinations

# Q4 Set Cover
def greedy_cover(U,S):
    left=set(U);out=[]
    while left:
        s=max(S,key=lambda x:len(set(x)&left));out.append(s);left-=set(s)
    return out
print("T7 Q4:",greedy_cover(range(1,8),[{1,2,3},{2,4},{3,4,5,6},{4,5},{5,6,7},{6,7}]))
