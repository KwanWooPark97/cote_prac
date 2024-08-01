a=list(input().rstrip())
r=[]
cnt=0
for i in a:
    if i not in r:
        r.append(i)
    else:
        if r[-1] != i:
            idx=r.index(i)
            cnt+=len(r)-idx-1
            r.pop(idx)
        else:
            r.pop()

print(cnt)