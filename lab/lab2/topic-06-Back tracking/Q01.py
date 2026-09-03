# DAA Lab Exercise
# Topic 6 - Backtracking - Question 1

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q1/Q2 N-Queens
def queens(n,cols=None,obs=set()):
    board=[-1]*n;ans=[]
    def safe(r,c):
        if c>=cols:return False
        if (r,c) in obs:return False
        return all(board[x]!=c and abs(board[x]-c)!=abs(x-r) for x in range(r))
    def bt(r):
        if r==n:ans.append(board[:]);return True
        for c in range(cols or n):
            if safe(r,c):
                board[r]=c
                if bt(r):return True
                board[r]=-1
        return False
    bt(0);return ans[0] if ans else None
print("T6 Q1:",queens(4))
print("T6 Q2:",queens(8,10),queens(5,5,{(2,2),(4,4)}),queens(6,6))
