import heapq
import sys
n=int(sys.stdin.readline())
p=[]
heapq.heapify(p)
for i in range(n):
    a=list(map(int,sys.stdin.readline().split()))
    for i in a:
        if len(p)<n:
            heapq.heappush(p,i)
        else:
            if p[0]<i:
                heapq.heappushpop(p,i)

print(heapq.heappop(p))

