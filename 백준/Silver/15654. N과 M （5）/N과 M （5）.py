n,m=map(int,input().split())
num=list(map(int,input().split()))

num.sort()

def dfs(s):
    if len(s)==m:
        print(*s)
        return

    for i in range(n):
        if num[i] in s:
            continue
        s.append(num[i])
        dfs(s)
        s.pop()

dfs([])