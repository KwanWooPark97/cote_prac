n=int(input())
date=[]
for _ in range(n):
    date.append(list(map(int,input().split())))
dp=[0]*(n+1)

for i in range(n):
    for j in range(i+date[i][0],n+1):
        if dp[j]<dp[i]+date[i][1]:
            dp[j]=dp[i]+date[i][1]
print(dp[-1])