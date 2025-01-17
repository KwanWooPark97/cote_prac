n,k,p,x=map(int,input().split())

num=[[0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
	[4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
	[3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
	[3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
	[4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
	[3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
	[2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
	[3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
	[1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
	[2, 4, 3, 1, 2, 1, 2, 3, 1, 0]]
answer=0
x=list(str(x))
x=['0']*(k-len(x))+x
def dfs(cnt,led,word):
    if cnt==k:
        re=int(''.join(word))
        if 1<=re<=n and re!=int(''.join(x)):
            global answer
            #print(re)
            answer+=1
        return

    now=int(x[cnt])

    for idx,i in enumerate(num[now]):
        if (led+i)>p:
            continue
        dfs(cnt+1,led+i,word+str(idx))

dfs(0,0,'')
print(answer)