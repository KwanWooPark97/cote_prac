n,k=map(int,input().split())

v=[]

for _ in range(n):
    v.append(list(map(int,input().split())))
answer=0

dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    weight,value=v[i-1]
    for j in range(1,k+1):
        if j>=weight:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1],dp[i-1][j-weight]+value)
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[n][k])