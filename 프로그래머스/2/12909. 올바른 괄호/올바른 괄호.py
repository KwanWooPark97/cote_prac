from collections import deque
def solution(s):
    answer = True
    
    s=deque(s)
    
    temp=[]
    while s:
        now=s.pop()
        if now==')':
            temp.append(now)
        elif now=='(':
            if not temp:
                return False
            temp.pop(-1)
    
    if temp:
        return False
    else:
        return True