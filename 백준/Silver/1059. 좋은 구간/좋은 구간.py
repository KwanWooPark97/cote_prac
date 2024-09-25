import bisect

l=int(input())
s=list(map(int,input().split()))
n=int(input())

s.sort()
if n in s:
    print(0)
    exit()
if s[0]>n:
    s.insert(0,0)
answer=0
idx=bisect.bisect_left(s,n)
answer+=((n-1)-(s[idx - 1]))*((s[idx])-n)
answer+=(s[idx])-(n+1)
print(answer)
