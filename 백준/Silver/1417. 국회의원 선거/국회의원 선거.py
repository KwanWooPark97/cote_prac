import heapq
n=int(input())
q=[]
for i in range(1,n+1):
    q.append(-int(input()))

r=-q[0]
q=q[1:]
heapq.heapify(q)
cnt=0

while q:
    a=heapq.heappop(q)

    if -a<r:
        break
    else:
        cnt+=1
        heapq.heappush(q,a+1)
        r+=1

print(cnt)