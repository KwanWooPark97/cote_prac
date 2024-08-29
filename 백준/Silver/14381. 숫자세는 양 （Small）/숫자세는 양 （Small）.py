n=int(input())

for i in range(1,n+1):
    a=int(input())
    if a==0:
        print('Case'+' #'+str(i)+': INSOMNIA')
        continue
    cnt=[0]*10
    b=1
    while True:
        c=str(a*b)
        for j in c:
            if cnt[int(j)]==0:
                cnt[int(j)]=1

        if sum(cnt)==10:
            answer=c
            break
        b+=1
    print('Case'+' #'+str(i)+': '+c)