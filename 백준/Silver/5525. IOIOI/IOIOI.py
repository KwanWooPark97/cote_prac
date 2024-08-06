from collections import Counter
import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

s=sys.stdin.readline().rstrip()

a='IO'*n+'I'
cnt=0

for i in range(m-(2*n)):
    b=s[i:(2*n+1)+i]
    if b==a:
        cnt+=1
print(cnt)

