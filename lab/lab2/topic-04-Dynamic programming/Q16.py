# DAA Lab Exercise
# Topic 4 - Dynamic Programming - Question 16

from math import inf

# Q15/Q16 Optimal BST
def obst(keys,freq):
    n=len(keys);dp=[[0]*(n+1) for _ in range(n+1)];root=[[0]*(n+1) for _ in range(n+1)]
    for i in range(n):dp[i][i+1]=freq[i];root[i][i+1]=i
    for L in range(2,n+1):
        for i in range(n-L+1):
            j=i+L;total=sum(freq[i:j]);dp[i][j]=min(dp[i][r]+dp[r+1][j]+total for r in range(i,j))
    return dp[0][n],root
print("T4 Q15:",obst(["A","B","C","D"],[.1,.2,.4,.3])[0])
print("T4 Q16:",obst([10,12,16,21],[4,2,6,3])[0])
