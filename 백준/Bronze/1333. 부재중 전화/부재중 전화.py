n,l,d=map(int,input().split())
dp=[]
for i in range(n):
    dp+=[1]*l
    dp+=[0]*5
dp+=[0]*d
#dp.pop(0)

for i in range(d,len(dp)+1,d):
    if dp[i]==0:
        print(i)
        break
else:
    print(i+d)

'''1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

1 3 20'''