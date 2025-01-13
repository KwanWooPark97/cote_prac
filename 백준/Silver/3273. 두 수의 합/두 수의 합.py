n=int(input())
a=list(map(int,input().split()))
x=int(input())

cnt=[0]*2000001

for i in range(n):
    cnt[a[i]]+=1

answer=0

for i in range(1,x//2+1):
    if cnt[i]!=0 and (x-i)!=i:
        answer+=cnt[i]*cnt[x-i]
        cnt[i]=0
        cnt[x-i]=0
print(answer)

'''
2
1 2
3
'''