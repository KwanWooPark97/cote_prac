import sys
n,m=map(int,sys.stdin.readline().split())

num=list(map(int,sys.stdin.readline().split()))
start=0
end=0
answer=0
cnt=num[0]

while True:
    if cnt==m:
        answer+=1
    if cnt<m:
        end+=1
        if end >=n:
            break
        cnt+=num[end]
    else:
        cnt-=num[start]
        start+=1

print(answer)
