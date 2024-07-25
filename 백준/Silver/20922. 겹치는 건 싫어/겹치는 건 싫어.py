n,k=map(int,input().split())

r=list(map(int,input().split()))
d={}
answer=0
start,end=0,0
while end<n:
    if r[end] not in d:
        d[r[end]]=1
        end+=1
        answer = max(end-start, answer)
    else:
        if d[r[end]]>=k:
            d[r[start]]-=1
            start+=1
        else:
            d[r[end]] += 1
            end += 1
            answer = max(end - start, answer)
print(answer)