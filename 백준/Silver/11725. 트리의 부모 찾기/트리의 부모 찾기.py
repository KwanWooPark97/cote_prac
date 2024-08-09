import sys
sys.setrecursionlimit(100000)
n=int(sys.stdin.readline())
adj=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

node=[False]*n
node[0]=True
par=[0]*n
def dfs(x):
    node[x]=True

    for i in adj[x]:
        if not node[i]:
            par[i]=x
            dfs(i)

dfs(0)
for i in par[1:]:
    print(i+1)