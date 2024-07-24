import heapq
import sys
n=int(sys.stdin.readline())

q=[]
for _ in range(n):
    a=int(sys.stdin.readline())
    if a==0:
        if len(q)==0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q,a)