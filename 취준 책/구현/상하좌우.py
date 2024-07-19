import time

N=input()

move=list(map(str,input().split()))

maxvalue=N
minvalue=1
x=1
y=1

for i in move:
    if (x==1 and i=='L') or (i=='U' and y==1):
        continue
    elif (x==maxvalue and i=='U') or (i=='R' and y==maxvalue):
        continue

    if i=='L':
        x -=1
    elif i=='R':
        x +=1
    elif i=='U':
        y -=1
    elif i=='D':
        y +=1

print(y,x)

#책과 거의 비슷함