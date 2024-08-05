import sys
from collections import deque
import heapq
n=int(sys.stdin.readline())
card=list()
for _ in range(n):
    card.append(int(sys.stdin.readline()))

heapq.heapify(card)

cnt=0
while len(card)!=1:
    a=heapq.heappop(card)+heapq.heappop(card)
    cnt+=a
    heapq.heappush(card,a)

print(cnt)


