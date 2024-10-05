n=int(input())
red=[[0]*4 for _ in range(4)]
blue=[[0]*6 for _ in range(4)]
green=[[0]*4 for _ in range(6)]
score=0
def green_drop(t,y,x):
    if t==1:
        for i in range(6):
            if green[i][x]!=0:
                green[i-1][x]=1
                break
        else:
            green[5][x]=1
    elif t==2:
        for i in range(6):
            if green[i][x]!=0 or green[i][x+1]!=0:
                green[i-1][x]=1
                green[i-1][x+1]=1
                break
        else:
            green[5][x]=1
            green[5][x+1]=1
    elif t==3:
        for i in range(6):
            if green[i][x]!=0:
                green[i-1][x]=1
                green[i-2][x]=1
                break
        else:
            green[5][x]=1
            green[4][x]=1

def blue_drop(t,y,x):
    if t == 1:
        for i in range(6):
            if blue[y][i] != 0:
                blue[y][i-1] = 1
                break
        else:
            blue[y][5] = 1
    elif t == 2:
        for i in range(5):
            if blue[y][i] != 0 or blue[y][i+1] != 0:
                blue[y][i-1] = 1
                blue[y][i] = 1
                break
        else:
            blue[y][5] = 1
            blue[y][4] = 1
    elif t == 3:
        for i in range(6):
            if blue[y][i] != 0 or blue[y+1][i]!=0:
                blue[y][i-1] = 1
                blue[y+1][i-1] = 1
                break
        else:
            blue[y][5] = 1
            blue[y+1][5] = 1
def clear(green,blue):
    global score
    for i in range(2,6):
        if sum(green[i])==4:
            green.pop(i)
            green.insert(0,[0, 0, 0, 0])
            score+=1

    cnt=0
    for i in range(2):
        if sum(green[i])>=1:
            cnt+=1
    for i in range(cnt):
        green.pop()
        green.insert(0,[0, 0, 0, 0])
    blue=list(map(list, zip(*blue[::-1])))
    for i in range(2,6):
        if sum(blue[i])==4:
            blue.pop(i)
            blue.insert(0,[0, 0, 0, 0])
            score+=1
    cnt = 0
    for i in range(2):
        if sum(blue[i]) >= 1:
            cnt += 1
    for i in range(cnt):
        blue.pop()
        blue.insert(0, [0, 0, 0, 0])
    blue=list(map(list, zip(*blue)))[::-1]

    return green,blue


for _ in range(n):
    t,y,x=map(int,input().split())
    green_drop(t,y,x)
    blue_drop(t,y,x)
    green,blue=clear(green,blue)
    
print(score)
g=0
b=0
for i in range(6):
    g+=sum(green[i])
for i in range(4):
    b+=sum(blue[i])
print(g+b)