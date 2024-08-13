from collections import deque
def solution(cards):
    answer = 0
    visited=[0]*len(cards)
    def bfs(x):
        q=deque()
        q.append(cards[x])
        visited[x]=1
        g=1
        while q:
            node=q.popleft()
            if visited[node]==0:
                q.append(cards[node])
                visited[node]=1
                g+=1
        return g
    for i in range(len(cards)):
        cards[i]-=1
    cnt=[]
    for i in range(len(cards)):
        if visited[i]==0:
            cnt.append(bfs(i))
            
    cnt.sort(reverse=True)
    
    if len(cnt)>=2:
        answer=cnt[0]*cnt[1]
    else:
        answer=0
    return answer