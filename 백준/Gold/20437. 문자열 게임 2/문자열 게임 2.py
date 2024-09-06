from collections import Counter

t=int(input())

for _ in range(t):
    short = 1e6
    long = 0
    w=input()
    k=int(input())
    a=Counter(w)
    pos=dict()
    for i in a.keys():
        if a[i]>=k:
            pos[i]=[]
    for i in range(len(w)):
        if w[i] in pos:
            pos[w[i]].append(i)

    for idx,val in pos.items():
        for i in range(len(val)-k+1):
            short=min(short,val[i+k-1]-val[i]+1)
            #1 3 5 7 9
            long=max(long,val[i+k-1]-val[i]+1)


    if long==0:
        print(-1)
    else:
        print(short,long)



