n=int(input())

r=list(map(int,input().split()))

r.sort()

cnt=0
answer=0
for i in r:
    cnt+=i
    answer+=cnt
print(answer)