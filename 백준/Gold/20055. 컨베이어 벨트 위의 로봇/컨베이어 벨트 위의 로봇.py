from collections import deque
n,k=map(int,input().split())

a=deque(map(int,input().split()))
robot=deque([0]*(2*n))

cnt=0

while a.count(0)<k:
    a.rotate(1)
    robot.rotate(1)

    if robot[n-1]:
        robot[n-1]=0

    for i in range(n-2,-1,-1):
        if robot[i]==1 and a[i+1]>=1 and robot[i+1]==0:
            a[i+1]-=1
            robot[i+1]=1
            robot[i]=0
            if (i+1)==(n-1):
                robot[i+1]=0

    if a[0]>=1:
        robot[0]=1
        a[0]-=1
    cnt+=1

print(cnt)
