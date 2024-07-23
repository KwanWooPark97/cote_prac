n,m=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(n)]

d=[-1,0,1]

re=1e9
def dfs(su,x,y,dir):
    if y==n-1:
        global re
        re=min(su,re)
        return

    for i in range(len(d)):
        if i==dir:
            continue
        new_x=x+d[i]
        if 0<=new_x<m:
            dfs(su+board[y+1][new_x],new_x,y+1,i)
for i in range(m):
    dfs(board[0][i],i,0,4)

print(re)