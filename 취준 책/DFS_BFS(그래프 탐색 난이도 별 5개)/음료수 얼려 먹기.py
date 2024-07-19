from collections import deque

n,m=map(int,input().split())

graph=[]
for i in range(n):
    data=list(map(int,input()))
    graph.append(data)

def dfs(x,y):
    if x<0 or y<0 or x>m-1 or y>n-1:
        return False

    elif graph[y][x]==0:
        graph[y][x]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

count=0

for i in range(n):
    for j in range(m):
        result=dfs(j,i)
        if result==True:
            count+=1

print(count)