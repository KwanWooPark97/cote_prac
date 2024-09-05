from collections import deque
t=[]
for i in range(4):
    t.append(deque(input().rstrip()))

n=int(input())
for _ in range(n):
    num,d=map(int,input().split())
    num-=1
    visited=[0]*4
    q=deque([])
    q.append(num)
    visited[num]=d
    while q:
        now=q.popleft()
        if 0<now and visited[now-1]==0 and t[now][-2]!=t[now-1][2]:
            q.append(now-1)
            visited[now-1]=-visited[now]
        if now<3 and visited[now+1]==0 and t[now][2]!=t[now+1][-2]:
            q.append(now+1)
            visited[now+1]=-visited[now]

    for i in range(4):
        if visited[i]!=0:
            t[i].rotate(visited[i])
answer=0

for i in range(1,5):
    if int(t[i-1][0]):
        answer+=int(t[i-1][0])*(2**(i-1))

print(answer)