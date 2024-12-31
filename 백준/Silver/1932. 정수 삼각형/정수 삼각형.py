n=int(input())
tri=[]
for _ in range(n):
    tri.append(list(map(int,input().split())))

dp=[[0]*(i+1) for i in range(n)]

dp[0][0]=tri[0][0]


for i in range(1,n):
    for j in range(i+1):
        left = 0
        right = 0
        if j>0:
            left=tri[i][j]+dp[i-1][j-1]
        if j<i:
            right=tri[i][j]+dp[i-1][j]

        dp[i][j]=max(left,right)

print(max(dp[-1]))


