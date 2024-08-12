from collections import deque
def solution(board):
    answer = 0
    visited=[[1e9]*len(board[0]) for _ in range(len(board))]
    
    def bfs():
        q=deque()
        q.append([0,0,0,-1])
        d=[[-1,0],[1,0],[0,-1],[0,1]]
        while q:
            y,x,cost,dd=q.popleft()
            for idx,val in enumerate(d):
                if (dd==0 and idx==1) or (dd==1 and idx==0) or (dd==2 and idx==3) or (dd==3 and idx==2):
                    continue
                new_x=x+val[0]
                new_y=y+val[1]
                if (2<=dd and idx<2) or (0<=dd<2 and idx>=2):
                    new_cost=cost+600
                else:
                    new_cost=cost+100
                    
                if 0<=new_x<len(board[0]) and 0<=new_y<len(board) and board[new_y][new_x]==0 and visited[new_y][new_x]>=new_cost-499:
                    q.append([new_y,new_x,new_cost,idx])
                    if visited[new_y][new_x]>new_cost:
                        visited[new_y][new_x]=new_cost
            
    bfs()
    answer=visited[-1][-1]
    for i in visited:
        print(i)
    return answer


'''
0 0 0 0 0
0 1 1 1 0
0 0 1 0 0
1 0 0 0 1
1 1 1 0 0'''