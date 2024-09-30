import bisect
n=int(input())

person=[]

for i in range(n):
    person.append(list(map(int,input().split())))

def func(y,x,d_1,d_2):
    board=[[0]*n for _ in range(n)]

    for i in range(d_1+1):
        board[y+i][x-i]=5
        board[y+d_2+i][x+d_2-i]=5
    for i in range(d_2+1):
        board[y+i][x+i]=5
        board[y+d_1+i][x-d_1+i]=5
    m=[0]*5

    for i in range(n):
        if board[i].count(5)==2:
            a=board[i].index(5)
            b=board[i].index(5,a+1)
            board[i][a:b]=[5]*(b-a)

        for j in range(n):
            if board[i][j]==5:
                m[4]+=person[i][j]
                continue
            if 0<=i<y+d_1 and 0<=j<=x:
                board[i][j]=1
                m[0]+=person[i][j]
            elif 0<=i<=y+d_2 and x<j<n:
                board[i][j] = 2
                m[1]+=person[i][j]
            elif y+d_1<=i<n and 0<=j<x-d_1+d_2:
                board[i][j] = 3
                m[2]+=person[i][j]
            elif y+d_2<i<n and x-d_1+d_2<=j<n:
                board[i][j] = 4
                m[3]+=person[i][j]

    '''if (max(m)-min(m))==15:
        print(y,x,d_1,d_2)
        for i in range(n):
            print(*board[i])
        print(m)'''
    return max(m)-min(m)

answer=1e9
for i in range(n):
    for j in range(n):
        for d_1 in range(n):
            for d_2 in range(n):
                if 0<=i<i+d_1+d_2<n and 0<=j-d_1<j<j+d_2<n:
                    answer=min(answer,func(i,j,d_1,d_2))
print(answer)