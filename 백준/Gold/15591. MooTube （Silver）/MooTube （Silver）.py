import sys
sys.setrecursionlimit(10000)
n,q=map(int,input().split())

adj=[[] for _ in range(n)]
for _ in range(n-1):
    a,b,c=map(int,input().split())
    adj[a-1].append([b-1,c])
    adj[b-1].append([a-1,c])

def dfs(now,cost):
    global cnt

    if cost!=1000000001 and cost>=k:
        cnt+=1
    visited[now]=True
    for i in range(len(adj[now])):
        n=adj[now][i][0]
        if visited[n]:
            continue
        dfs(n,min(cost,adj[now][i][1]))

for _ in range(q):
    cnt=0
    k,v= map(int, input().split())
    v-=1
    visited=[False]*n
    dfs(v,1000000001)
    print(cnt)
