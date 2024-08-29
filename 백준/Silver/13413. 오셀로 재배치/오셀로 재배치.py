t=int(input())

for _ in range(t):
    q = []
    n=int(input())
    a=list(input())
    b=list(input())
    cnt=0
    for i in range(n):
        if a[i]!=b[i]:
            if len(q)==0 or q[-1]==a[i]:
                q.append(a[i])
            elif q[-1]!=a[i]:
                q.pop()
                cnt+=1
    cnt+=len(q)
    print(cnt)