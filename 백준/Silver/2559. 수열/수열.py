n,k=map(int,input().split())

a=list(map(int,input().split()))

r=[]

r.append(sum(a[:k]))

for i in range(n-k):
    r.append(r[i]-a[i]+a[i+k])
print(max(r))