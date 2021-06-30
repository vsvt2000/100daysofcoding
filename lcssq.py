def solve(str1,str2):
    n=len(str1)
    m=len(str2)
    dp=[[0]*(m+1) for i in range (n+1)]
    for i in range(n):
        for j in range(m):
            if str1[i]==str2[j]:
                dp[i+1][j+1]=dp[i][j]+1
            else:
                dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
    return dp[-1][-1]
