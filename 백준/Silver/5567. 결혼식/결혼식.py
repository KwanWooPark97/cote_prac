from collections import deque
n=int(input())

f=int(input())
adj=[[] for _ in range(n)]
for _ in range(f):
    a,b=map(int,input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

visited=[0]*n

q=deque([0])

visited[0]=1
while q:
    now=q.popleft()

    for i in adj[now]:
        if visited[i]==0:
            visited[i]=visited[now]+1
            if visited[i]!=3:
                q.append(i)

answer=0
for i in visited[1:]:
    if i:
        answer+=1
print(answer)
