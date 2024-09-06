from collections import Counter
#3 1 2 3  5
h,w=map(int,input().split())
water=list(map(int,input().split()))
answer=0
for i in range(1,w-1):
    left=max(water[:i])
    right=max(water[i+1:])
    w=min(left,right)
    if water[i]<w:
        answer+=w-water[i]
print(answer)
