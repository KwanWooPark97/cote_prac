n,s=map(int,input().split())

r=list(map(int,input().split()))
visited=[]
answer=0

def dfs(cnt,depth):
    if cnt and sum(cnt)==s:
        global answer
        answer+=1

    for i in range(depth,n):
        cnt.append(r[i])
        dfs(cnt,i+1)
        cnt.pop()

dfs(visited,0)
print(answer)