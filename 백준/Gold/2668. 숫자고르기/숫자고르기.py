import copy
n=int(input())

adj=[[] for i in range(n)]
for i in range(n):
    p=int(input())-1
    adj[p].append(i)
answer=[]
visited=[0]*n
def dfs(i,g):
    visited[i]=1
    for j in adj[i]:
        g.add(i)
        if visited[j]==1:
            answer.extend(list(g))
            return
        dfs(j,copy.deepcopy(g))
    visited[i]=0
for i in range(n):
    if visited[i]==0:
        dfs(i,set([]))
answer=list(set(answer))
answer.sort()
print(len(answer))
for i in answer:
    print(i+1)


