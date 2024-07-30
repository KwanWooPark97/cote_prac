import sys
n,m=map(int,sys.stdin.readline().split())

a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))

re=sorted(a+b)

for i in re:
    print(i,end=' ')
