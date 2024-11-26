from collections import deque
def solution(s):
    answer = -1
    s=deque(s)
    tmp=deque()
    tmp.append(s.popleft())
    while s:
        now=s.popleft()
        if tmp and tmp[-1]==now:
            tmp.pop()
        else:
            tmp.append(now)
    if tmp:
        return 0
    else:
        return 1
    #return answer