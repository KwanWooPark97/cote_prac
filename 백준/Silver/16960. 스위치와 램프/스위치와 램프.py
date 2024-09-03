from itertools import combinations as cb
import sys
n,m=map(int,input().split())

adj=[[] for _ in range(n)]

for i in range(n):
    a=list(map(int,sys.stdin.readline().split()))
    adj[i]+=a[1:]

c=[i for i in range(n)]

a=list(cb(c,n-1))

for i in a:
    sw=[0]*(m+1)
    for j in i:
        for k in adj[j]:
            if sw[k]==0:
                sw[k]=1
    if sum(sw)==m:
        print(1)
        break
else:
    print(0)
