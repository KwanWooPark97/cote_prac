import heapq

n=int(input())

num={}
for _ in range(n):
    d,w=map(int,input().split())
    num.setdefault(d,[]).append(w)

result=[]
answer=0
for i in range(1001,0,-1):
    if i in num:
        for j in num[i]:
            heapq.heappush(result,-j)
    if len(result)>0:
        
        answer+=-heapq.heappop(result)


print(answer)