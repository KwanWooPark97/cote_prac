import sys
n=int(sys.stdin.readline())

color=[0]+list(map(int,sys.stdin.readline().split()))
answer=0
for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    if color[a]!=color[b]:
        answer+=1
if color[1]!=0:
    answer+=1
print(answer)