import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
par=list(map(int,sys.stdin.readline().rstrip().split()))
s=[0]*n
for i in range(n):
    if par[i]==-1:
        continue
    par[i]-=1
for _ in range(m):
    num,r=map(int,sys.stdin.readline().rstrip().split())
    s[num-1]+=r

def find_par(x,cnt):
    if x==0:
        return cnt
    return find_par(par[x],cnt+s[x])
reward=[0]*n
for i in range(n):
    if i==0:
        continue
    reward[i]=reward[par[i]]+s[i]

for i in reward:
    print(i,end=' ')
