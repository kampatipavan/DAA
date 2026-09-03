def champagne(poured,row,glass):
    dp=[[0.0]*101 for _ in range(101)]; dp[0][0]=poured
    for r in range(100):
        for c in range(r+1):
            excess=max(0.0,(dp[r][c]-1)/2)
            dp[r+1][c]+=excess; dp[r+1][c+1]+=excess
    print(f"{min(1.0,dp[row][glass]):.5f}")
champagne(1,1,1); champagne(2,1,1)
