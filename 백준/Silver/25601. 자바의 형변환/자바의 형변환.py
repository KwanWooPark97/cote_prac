from collections import deque
n=int(input())
name=set()
graph=[]
for i in range(n-1):
    j,p=input().split()
    name.update([j])
    name.update([p])
    graph.append([j,p])

f_a,f_b=input().split()
name=list(name)

dic={val:idx for idx,val in enumerate(name)}
adj=[[] for _ in range(n)]
for i in range(n-1):
    j,p=graph[i]
    adj[dic[p]].append(dic[j])

def find_par(a,b):
    q=deque([])
    q.append(a)
    while q:
        now=q.popleft()
        if now==b:
            return 1
        for i in adj[now]:
            q.append(i)

    return 0

if find_par(dic[f_a],dic[f_b]) or find_par(dic[f_b],dic[f_a]):
    print(1)
else:
    print(0)