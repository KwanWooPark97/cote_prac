n=int(input())

par=list(map(int,input().split()))

node=int(input())

def get_parent(x,node):
    if par[x] == -1 or par[x]==node:
        return par[x]
    return get_parent(par[x],node)
black=[0]*n
for i in range(n):
    if i==node:
        black[i]=1
        continue
    if get_parent(i,node)==node:
        black[i]=1

red=[0]*n
for i in range(n):
    if black[i] or par[i]==-1:
        continue
    red[par[i]]=1

answer=0

for i in range(n):
    if black[i]==0 and red[i]==0:
        answer+=1

print(answer)