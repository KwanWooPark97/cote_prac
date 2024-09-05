def dfs(ns,depth):
    if len(ns)==6:
        print(*ns)
        return
    for i in range(depth,n):
        ns.append(num[i])
        dfs(ns,i+1)
        ns.pop()

while True:
    r=list(map(int,input().split()))
    if r[0]==0:
        break
    num=r[1:]
    n=r[0]
    dfs([],0)
    print('')