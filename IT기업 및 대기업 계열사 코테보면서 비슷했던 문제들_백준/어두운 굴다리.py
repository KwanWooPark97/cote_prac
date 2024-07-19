n=int(input())

m=int(input())

p=list(map(int,input().split()))

p=p
answer=0
cnt=0
for i in range(len(p)-1):
    if (p[i+1]-p[i])%2==0:
        cnt=(p[i+1]-p[i])//2
    else:
        cnt = (p[i + 1] - p[i]) // 2 +1
    answer=max(answer,cnt)

re=[answer,p[0],n-p[-1]]
print(max(re))


