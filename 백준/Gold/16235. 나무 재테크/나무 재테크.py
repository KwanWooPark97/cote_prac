import sys
from collections import deque
n,m,k=map(int,sys.stdin.readline().split())
board=[]
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))

yang=[[5]*n for _ in range(n)]
tree = [[deque() for _ in range(n)] for _ in range(n)]
for i in range(m):
    y,x,a=map(int,sys.stdin.readline().split())
    tree[y-1][x-1].append(a)

for _ in range(k):
    f=[]
    for i in range(n):
        for j in range(n):
            dead=0
            new_tree = deque([])
            for _ in range(len(tree[i][j])):
                a=tree[i][j].popleft()
                if yang[i][j]<a:
                    dead += a // 2
                    for k in tree[i][j]:
                        dead+=k//2
                    break
                else:
                    yang[i][j]-=a
                    new_tree.append(a+1)
                    if (a+1)%5==0:
                        f.append([i,j])
            tree[i][j]=new_tree
            yang[i][j]+=dead
    dx=[0,0,1,-1,-1,1,-1,1]
    dy=[1,-1,0,0,1,-1,-1,1]
    for i in range(len(f)):
        for j in range(8):
            new_x=f[i][1]+dx[j]
            new_y=f[i][0]+dy[j]
            if 0<=new_x<n and 0<=new_y<n:
                tree[new_y][new_x].appendleft(1)

    for i in range(n):
        for j in range(n):
            yang[i][j]+=board[i][j]


answer=0
for i in range(n):
    for j in range(n):
        answer+=len(tree[i][j])
print(answer)