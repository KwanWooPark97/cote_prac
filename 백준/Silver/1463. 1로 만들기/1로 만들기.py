from collections import deque
n=int(input())
q=deque()
q.append([n,0])
visited=[0]*n
if n==1:
    print(0)
else:
    while q:
        a,cnt=q.popleft()
        if a%3==0 and (visited[a//3]==0 or visited[a//3]>cnt):
            if a//3==1:
                print(cnt+1)
                break
            visited[a//3]=cnt
            q.append([a//3,cnt+1])
        if a%2==0 and (visited[a//2]==0 or visited[a//2]>cnt):
            if a//2==1:
                print(cnt+1)
                break
            visited[a//2]=cnt
            q.append([a//2,cnt+1])
        if a==2:
            print(cnt+1)
            break
        if (visited[a-1]==0 or visited[a-1]>cnt):
            visited[a-1]=cnt
            q.append([a-1,cnt+1])

