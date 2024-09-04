import copy
import sys
from collections import deque
n,c=map(int,sys.stdin.readline().split())
r=list(map(int,sys.stdin.readline().split()))

dp_pre=[0 for i in range(n)]
dp_suf=[0 for i in range(n)]

for i in range(1,n):
    dp_pre[i]=dp_pre[i-1]
    if r[i-1] >=r[i]:
        dp_pre[i]+= r[i-1]-r[i]
    else:
        dp_pre[i]+= c-r[i]+r[i-1]

for i in range(n-1)[::-1]:
    dp_suf[i]=dp_suf[i+1]
    if r[i+1] >=r[i]:
        dp_suf[i]+= r[i+1]-r[i]
    else:
        dp_suf[i]+= c-r[i]+r[i+1]

answer=1e60
idx=0
for i in range(n):
    answer=min(answer,max(dp_pre[i],dp_suf[i]))
for i in range(n):
    if max(dp_pre[i],dp_suf[i])==answer:
        idx=i+1
        break
print(idx)
print(answer)