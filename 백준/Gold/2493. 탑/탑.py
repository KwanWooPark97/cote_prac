import heapq

n=int(input())
top=list(map(int,input().split()))[::-1]
answer=[0]*n
q=[[top[0],0]]
heapq.heapify(q)
for i in range(1,n):
    while q and q[0][0]<top[i]:
        _,idx=heapq.heappop(q)
        answer[len(top)-idx-1]=len(top)-i
    heapq.heappush(q,[top[i],i])
print(*answer)
#4 7 5 9 6