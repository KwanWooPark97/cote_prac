import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
node,edge=map(int,sys.stdin.readline().split())
graph=[]
for _ in range(edge):
    graph.append(list(map(int,sys.stdin.readline().split())))

graph.sort(key=lambda x:x[2])

par=[i for i in range(node+1)]
cnt=0
def find_par(x):
    if x != par[x]:
        par[x]=find_par(par[x])
    return par[x]

for i in graph:
    s_par=find_par(i[0])
    e_par=find_par(i[1])
    if s_par!=e_par:
        if s_par>e_par:
            par[s_par]=e_par
        else:
            par[e_par]=s_par
        cnt+=i[2]
    
print(cnt)