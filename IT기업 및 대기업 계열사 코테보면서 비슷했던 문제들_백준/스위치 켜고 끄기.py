n=int(input())

sw=list(map(int,input().split()))

stu=int(input())

stu_list=[list(map(int,input().split())) for _ in range(stu)]

for s,p in stu_list:

    if s==1:
        for i in range(p-1,len(sw),p):
            if sw[i]==0:
                sw[i]=1
            else:
                sw[i]=0

    else:
        i=1
        a=''.join(list(map(str,sw)))
        p-=1
        while (p-i)>=0 and p+i+1<=len(a):
            if a[p-i:p+i+1]==a[p-i:p+i+1][::-1]:
                i+=1
            else:
                i-=1
                for j in range(p-i,p+i+1):
                    if sw[j] == 0:
                        sw[j] = 1
                    else:
                        sw[j] = 0
                break
        else:
            i -= 1
            for j in range(p - i, p + i + 1):
                if sw[j] == 0:
                    sw[j] = 1
                else:
                    sw[j] = 0
for i in range(len(sw)):
    if (i+1)%20==0:
        print(sw[i])
    else:
        print(sw[i], end=' ')