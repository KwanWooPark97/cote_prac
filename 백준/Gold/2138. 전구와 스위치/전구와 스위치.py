import copy
import sys
input=sys.stdin.readline
n=int(input())
now=list(map(int,input().rstrip()))
want=list(map(int,input().rstrip()))
answer=0
pre_answer=1
#0을 먼저 눌럿다.
pre_check=copy.deepcopy(now)
pre_check[0]=1-pre_check[0]
pre_check[1]=1-pre_check[1]
#0을 안누르고 시작

post_check=copy.deepcopy(now)
post_answer=0

for i in range(1,n):
    if pre_check[i - 1] != want[i - 1]:
        pre_check[i-1]=1-pre_check[i-1]
        pre_check[i]=1-pre_check[i]
        if i!=(n-1):
            pre_check[i+1]=1-pre_check[i+1]
        pre_answer += 1

if pre_check==want:
    answer=pre_answer
else:
    answer=1e9
for i in range(1,n):
    if post_check[i-1]!=want[i-1]:
        post_check[i-1]=1-post_check[i-1]
        post_check[i]=1-post_check[i]
        if i!=(n-1):
            post_check[i+1]=1-post_check[i+1]
        post_answer+=1

if post_check==want:
    answer=min(answer,post_answer)


if answer==1e9:
    print(-1)
else:
    print(answer)