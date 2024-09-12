import copy
n=int(input())

board=[]

for i in range(n):
    board.append(list(map(int,input().split())))

def up(b):
    for j in range(n):
        cursor=0
        for i in range(1,n):
            if b[i][j]!=0:
                temp=b[i][j]
                b[i][j]=0
                if b[cursor][j]==0:
                    b[cursor][j]=temp
                elif b[cursor][j]==temp:
                    b[cursor][j]=temp*2
                    cursor+=1
                else:
                    cursor+=1
                    b[cursor][j]=temp
    return b

def down(b):
    for j in range(n):
        cursor=n-1
        for i in range(n-1)[::-1]:
            if b[i][j]!=0:
                temp=b[i][j]
                b[i][j]=0
                if b[cursor][j]==0:
                    b[cursor][j]=temp
                elif b[cursor][j]==temp:
                    b[cursor][j]=temp*2
                    cursor-=1
                else:
                    cursor-=1
                    b[cursor][j]=temp
    return b

def left(b):
    for i in range(n):
        cursor=0
        for j in range(1,n):
            if b[i][j]!=0:
                temp=b[i][j]
                b[i][j]=0
                if b[i][cursor]==0:
                    b[i][cursor]=temp
                elif b[i][cursor]==temp:
                    b[i][cursor]=temp*2
                    cursor+=1
                else:
                    cursor+=1
                    b[i][cursor]=temp
    return b

def right(b):
    for i in range(n):
        cursor=n-1
        for j in range(n-1)[::-1]:
            if b[i][j]!=0:
                temp=b[i][j]
                b[i][j]=0
                if b[i][cursor]==0:
                    b[i][cursor]=temp
                elif b[i][cursor]==temp:
                    b[i][cursor]=temp*2
                    cursor-=1
                else:
                    cursor-=1
                    b[i][cursor]=temp
    return b
answer=0
def dfs(b,deep):
    if deep==5:
        global answer
        for i in range(n):
            answer=max(max(b[i]),answer)
        return
    a=copy.deepcopy(b)
    dfs(down(a),deep+1)
    a = copy.deepcopy(b)
    dfs(up(a), deep + 1)
    a = copy.deepcopy(b)
    dfs(right(a), deep + 1)
    a = copy.deepcopy(b)
    dfs(left(a), deep + 1)
dfs(copy.deepcopy(board),0)
print(answer)
