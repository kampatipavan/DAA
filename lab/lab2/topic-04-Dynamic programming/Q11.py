# DAA Lab Exercise
# Topic 4 - Dynamic Programming - Question 11

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q11 WordFilter
class WordFilter:
    def __init__(self,words):self.words=words
    def f(self,pref,suff):
        for i in range(len(self.words)-1,-1,-1):
            if self.words[i].startswith(pref) and self.words[i].endswith(suff):return i
        return -1
print("T4 Q11:",WordFilter(["apple"]).f("a","e"))
