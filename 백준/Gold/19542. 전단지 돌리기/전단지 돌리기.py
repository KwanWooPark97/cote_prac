import sys
sys.setrecursionlimit(100010)
n,s,d=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
h=[0]*n
answer=0
def dfs(cur,prv):
    for i in graph[cur]:
        if i==prv:
            continue
        dfs(i,cur)
        h[cur]=max(h[cur],h[i]+1)

def dfs2(cur,prv):
    global answer
    for i in graph[cur]:
        if i==prv or h[i]<d:
            continue
        answer+=2
        dfs2(i,cur)

dfs(s-1,-1)
dfs2(s-1,-1)
print(answer)


