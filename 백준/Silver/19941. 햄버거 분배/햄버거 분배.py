from collections import deque
n,k=map(int,input().split())

r=list(input())
cnt=0
for i in range(len(r)):
    if r[i]=='P':
        for j in range(max(i-k,0),min(i+k+1,len(r))):
            if r[j]=='H':
                r[j]='x'
                cnt+=1
                break
print(cnt)


