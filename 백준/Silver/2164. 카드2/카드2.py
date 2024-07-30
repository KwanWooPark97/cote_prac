import sys
from collections import deque

n=int(sys.stdin.readline())

card=deque([i for i in range(1,n+1)])
if n==1:
    card.append(1)

while True:
    card.popleft()
    if len(card)==1:
        print(card[0])
        break
    card.append(card.popleft())
