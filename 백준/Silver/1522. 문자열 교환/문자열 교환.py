from collections import deque
s=input().rstrip()
cnt=s.count('a')
s+=s
q=deque(s[:cnt])
s=deque(s[cnt:])
answer=1e9
while s:
    answer=min(q.count('b'),answer)
    q.append(s.popleft())
    q.popleft()

print(answer)
