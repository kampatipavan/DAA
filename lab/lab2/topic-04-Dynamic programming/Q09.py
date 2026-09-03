# DAA Lab Exercise
# Topic 4 - Dynamic Programming - Question 9

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q8/Q9 Word Break
def word_break(s,words):
    w=set(words); dp=[False]*(len(s)+1); dp[0]=True
    for i in range(1,len(s)+1):
        dp[i]=any(dp[j] and s[j:i] in w for j in range(i))
    return dp[-1]
def word_path(s,words):
    w=set(words); dp=[None]*(len(s)+1); dp[0]=[]
    for i in range(1,len(s)+1):
        for j in range(i):
            if dp[j] is not None and s[j:i] in w: dp[i]=dp[j]+[s[j:i]];break
    return dp[-1]
print("T4 Q8:",word_break("leetcode",["leet","code"]))
D=["i","like","sam","sung","samsung","mobile","ice","cream","icecream","man","go","mango"]
print("T4 Q9:",word_path("ilike",D),word_path("ilikesamsung",D))
