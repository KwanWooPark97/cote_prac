t=int(input())

for _ in range(t):
    n,k,idt,m=map(int,input().split())
    board=[[0]*(k+1) for _ in range(n+1)]
    teams={k:[] for k in range(1,n+1)}
    for i in range(m):
        team,prob,score=map(int,input().split())
        board[team][prob]=max(board[team][prob],score)
        teams[team].append(i)
    you=sum(board[idt])
    result=[]
    for j in range(1,n+1):
        result.append([j,sum(board[j]),teams[j]])

    result.sort(key=lambda x:(-x[1],len(x[2]),x[2][-1]))

    for idx,val in enumerate(result):
        if val[0]==idt:
            print(idx+1)
            break




