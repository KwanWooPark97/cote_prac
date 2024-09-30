import sys
from collections import deque
s=list(sys.stdin.readline().rstrip())
if s==s[::-1]:
    s.pop()
    if s==s[::-1]:
        print(-1)
    else:
        print(len(s))
else:
    print(len(s))