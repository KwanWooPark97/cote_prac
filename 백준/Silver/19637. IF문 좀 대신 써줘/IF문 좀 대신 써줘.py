import sys
from bisect import bisect_left as bl
n,m=map(int,sys.stdin.readline().split())

name={}
strong=[]

for i in range(n):
    a,b=sys.stdin.readline().split()
    name[i]=a
    strong.append(int(b))

for _ in range(m):
    now=int(sys.stdin.readline())
    idx=bl(strong,now)
    print(name[idx])