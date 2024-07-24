n=int(input())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))
g=[0]*(1001)
a.sort(key=lambda x:x[0])
high=max(a,key=lambda x:x[1])
for i in a:
    g[i[0]]=i[1]
h=a[0][1]
answer=0
for i in range(a[0][0],high[0]):
    h=max(g[i],h)
    answer+=h
h=a[-1][1]
for i in range(a[-1][0],high[0],-1):
    h=max(g[i],h)
    answer+=h
answer+=high[1]
print(answer)