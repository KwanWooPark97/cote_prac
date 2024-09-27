import copy
n=int(input())

word=[]
for i in range(n):
    word.append(input().rstrip())
answer=0
cache=[[-1]*(2**n) for _ in range(n)]
def dp(last,mask):
    if cache[last][mask] !=-1:
        return cache[last][mask]
    ret=len(word[last])
    for i in range(n):
        if i==last:
            continue
        if mask &(2**i) !=0 and word[i][-1]==word[last][0]:
            ret=max(ret,len(word[last])+dp(i,mask-(2**last)))
    cache[last][mask]=ret
    return ret
for i in range(n):
    answer=max(answer,dp(i,2**n-1))

print(answer)