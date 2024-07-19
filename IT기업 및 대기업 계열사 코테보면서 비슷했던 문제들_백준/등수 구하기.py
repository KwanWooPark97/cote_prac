import bisect

n,score,p=map(int,input().split())

if n==0:
    print(1)
else:
    idx=0
    s = list(map(int, input().split()))
    if len(s)==p and s[-1]>=score:
        print(-1)
    else:
        for i in range(len(s)):
            if s[i]<=score:
                idx=i+1
                break
        else:
            idx=i+2

        print(idx)