import copy
n=list(map(int,input().split()))


start=0

while True:
    a=copy.deepcopy(n)
    if a[0] <start:
        r=start-a[0]
        if a[1] <r:
            break
        a[0],a[1]=start,a[1]-r
    if a[-1] <start:
        r=start-a[-1]
        if a[-2] <r:
            break
        a[-1],a[-2]=start,a[-2]-r

    a[2]+=a[1]+a[-2]

    if a[2]<start:
        break

    start+=1
print(start-1)