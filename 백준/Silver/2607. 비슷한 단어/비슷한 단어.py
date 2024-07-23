from collections import Counter

n=int(input())

re=[list(input()) for _ in range(n)]

a=Counter(re[0])
c=set(a.keys())
cnt=0
for i in range(1,n):
    b=Counter(re[i])
    if a==b:
        cnt+=1
        continue
    if len(list(re[0]))>len(re[i]):
        e=a-b
    else:
        e=b-a
    if len(e.keys())==1 and list(e.values())[0]==1:
        cnt+=1
    
print(cnt)