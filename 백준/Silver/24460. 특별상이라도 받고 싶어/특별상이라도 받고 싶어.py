n=int(input())
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

def div(x,y,l):
    if l==1:
        return board[y][x]
    r=[]
    r.append(div(x,y,l//2))
    r.append(div(x,y+l//2,l//2))
    r.append(div(x+l//2,y,l//2))
    r.append(div(x+l//2,y+l//2,l//2))
    r.sort()
    return r[1]

print(div(0,0,n))


'''
15 7    13 5
4 2     1 9

0 10    8 12
3 11    14 6

div(0,0,4)
=>div(0,0,2), div(0,2,2), recur(2,0,2), recur(2,2,2)
l을 2로 나누고 더한 재귀들 실행
'''