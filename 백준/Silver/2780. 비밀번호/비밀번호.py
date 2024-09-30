import sys
t=int(sys.stdin.readline())
d=[[7],[2,4],[1,3,5],[2,6],[1,5,7],[2,4,6,8],[3,5,9],[4,8,0],[5,7,9],[6,8]]

answer=0
dp=[[0 for _ in range(10)] for _ in range(1001)]

for i in range(10):
    dp[1][i]=1
for i in range(2,1001):
    for j in range(10):
        for k in d[j]:
            dp[i][j]+=dp[i-1][k]
            dp[i][j]%=1234567

for _ in range(t):
    n=int(sys.stdin.readline())
    print(sum(dp[n])%1234567)
