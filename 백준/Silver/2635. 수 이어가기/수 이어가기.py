n=int(input())

answer=[]

for i in range(n,-1,-1):
    t=[n,i]
    while t[-1]>=0:
        t.append(t[-2]-t[-1])
    t.pop()
    if len(t)>len(answer):
        answer=t
print(len(answer))
print(*answer)