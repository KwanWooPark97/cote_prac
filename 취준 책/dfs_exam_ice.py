import sys

def check(visted,start,graph):

    nx=[[-1,0],[1,0],[0,-1],[0,1]]
    visted[start[0]][start[1]]=True
    for i,j in nx:
        y=start[0]+i
        x=start[1]+j
        if y>=0 and y<=len(graph)-1 and x>=0 and x<=len(graph[0])-1 and graph[y][x] !=1 and visted[y][x]==False:
            visted[y][x]=True
            check(visted,[y,x],graph)


N,M=map(int,sys.stdin.readline().split())
graph=[]
visted=[[False for i in range(M)] for j in range(N)]
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))
count=0

for i in range(N):
    for j in range(M):
        if graph[i][j]==0 and visted[i][j]==False:
            check(visted,[i,j],graph)
            count+=1
            print(visted)
print(count)