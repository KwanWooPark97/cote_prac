l,c=map(int,input().split())

r=list(input().split())
r.sort()
def dfs(s,depth):
    if len(s)==l:
        m = ["a", "e", "i", "o", "u"]
        ans = 0
        for i in s:
            if i in m:
                ans += 1
        if ans>=1 and len(s)-ans>=2:
            print(''.join(s))
        return

    for i in range(depth,c):
        s.append(r[i])
        dfs(s,i+1)
        s.pop()

dfs([],0)