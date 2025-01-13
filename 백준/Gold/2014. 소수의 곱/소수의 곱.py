import heapq
import copy
k,n=map(int,input().split())

c=list(map(int,input().split()))

heap=copy.deepcopy(c)
heapq.heapify(heap)

for _ in range(n):
    now=heapq.heappop(heap)

    for i in c:
        if i*now>=2**31:
            break
        heapq.heappush(heap,i*now)
        if now%i==0:
            break
print(now)