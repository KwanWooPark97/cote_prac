def solution(n):
    answer = [[0]*n for _ in range(n)]
    row=0
    col=0
    cnt=1
    flag=1
    while flag:
        flag=0
        while True:
            answer[row][col]=cnt
            if (row+1)==n or answer[row+1][col]!=0:
                break
            row+=1
            cnt+=1
            flag=1
        while True:
            answer[row][col]=cnt
            if (col+1)==(row+1) or answer[row][col+1]!=0:
                break
            col+=1
            cnt+=1
            flag=1
        while True:
            answer[row][col]=cnt
            if ((row-1)==-1 or (col-1)==-1) or answer[row-1][col-1]!=0:
                break
            col-=1
            row-=1
            cnt+=1
            flag=1
    final=[]
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            if answer[i][j]!=0:
                final.append(answer[i][j])
    return final



'''

1

1
2 3

1
2 6
3 4 5

1 8 9
2 6 7
3 4 5


'''