n=int(input())

flower=list(map(int,input().split()))

dp=[0 for i in range(n+1)]

pos=[-1 for i in range(101)]

for i in range(n):
    for j in range(101):
        if pos[j]==-1:
            continue
        dp[i]=max(dp[i],dp[pos[j]]+(flower[pos[j]]-flower[i])**2)

    pos[flower[i]]=i

print(max(dp))