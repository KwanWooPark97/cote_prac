import sys
t=int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    p=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    p.sort(key=lambda x: x[0])
    cnt=0
    d=n+1
    for i in p:
        if i[1]<d:
            cnt+=1
            d=min(d,i[1])
    print(cnt)