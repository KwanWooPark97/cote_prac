n,m=map(int,input().split())

r=list(map(int,input().split()))

start=max(r)
end=sum(r)
re=0
while start<=end:
    answer=[]
    cnt=0
    mid=(start+end)//2

    for i in r:
        if cnt+i>mid:
            answer.append(cnt)
            cnt=0
        cnt+=i
    else:
        if cnt<=mid:
            answer.append(cnt)
    if len(answer)<=m:
        end=mid-1
        re=mid
    else:
        start=mid+1
print(re)