# DAA Lab Exercise
# Topic 6 - Backtracking - Question 17

from collections import Counter

# Q17 Universal Strings
def universal(a,b):
    req=Counter()
    for x in b:req|=Counter(x)
    return [x for x in a if all(Counter(x)[c]>=n for c,n in req.items())]
W=["amazon","apple","facebook","google","leetcode"]
print("T6 Q17:",universal(W,["e","o"]),universal(W,["l","e"]))
