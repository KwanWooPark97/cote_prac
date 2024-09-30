import sys
t=int(sys.stdin.readline())

for _ in range(t):
    n=int(sys.stdin.readline())

    cnt=0
    x=5
    while x<=n:
        cnt+=n//x
        x*=5

    print(cnt)