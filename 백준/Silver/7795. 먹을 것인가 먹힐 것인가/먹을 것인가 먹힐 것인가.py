t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()

    answer=0
    start=0
    end=0
    cnt=0
    while start<n:
        while a[start]>b[end]:
            cnt+=1
            end+=1
            if end==m:
                break
        answer+=cnt
        if end == m :
            break
        start+=1
    else:
        start-=1
    answer+=(n-start-1)*cnt
    print(answer)

