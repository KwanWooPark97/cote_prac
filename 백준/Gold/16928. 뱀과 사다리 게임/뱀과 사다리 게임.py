n,m=map(int,input().split())

sadari={}
snake= {}

for _ in range(n):
    a,b=map(int,input().split())
    sadari[a]=b
for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b

visited=[0]*101
for i in range(2):
    visited[i]=1
def dfs(cnt,now):
    if now==100:
        if visited[100]==0 or visited[100]>cnt:
            visited[100]=cnt
        return
    for i in range(1,7):
        board=now+i
        if board>100:
            break
        if board in sadari:
            board=sadari[board]
        elif board in snake:
            board=snake[board]
        if visited[board]==0 or visited[board]>cnt:
            visited[board]=cnt
            dfs(cnt+1,board)

dfs(1,1)
#print(visited)
print(visited[100])