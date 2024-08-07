n=int(input())

s=input()

start=1
end=n-1

mod=1e9+7
po=[0]*n
po[0]=1
cnt=0
for i in range(1,n):
    po[i]=po[i-1]*31%mod
while start <= end:
    mid=(start+end)//2
    start_hash=0
    for i in range(mid):
        start_hash *=31%mod
        start_hash+=ord(s[i])-ord('a')+1
        start_hash%=mod
    re=0
    p_hash = {}
    for i in range(n-mid+1):
        if start_hash in p_hash:
            for j in p_hash[start_hash]:
                if s[j:j+mid]==s[i:i+mid]:
                    re=1
                    break
            p_hash[start_hash].append(i)
            if re:
                break
        else:
            p_hash[start_hash]=[i]
        start_hash+=mod-(ord(s[i])-ord('a')+1)*po[mid-1]
        start_hash %= mod
        start_hash *=31%mod
        if i+mid <n:
            start_hash+=ord(s[i+mid])-ord('a')+1
            start_hash %= mod
    if re:
        cnt=mid
        start=mid+1
    else:
        end=mid-1
print(cnt)