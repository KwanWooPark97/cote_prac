import copy
n=int(input())
ca=[0]*100
cb=[0]*100
for i in range(n):
    a,b=map(int,input().split())
    ca[a]+=1
    cb[b]+=1
    answer=0
    point_a=0
    point_b=99
    now_a=copy.deepcopy(ca)
    new_b=copy.deepcopy(cb)
    while point_a<100 and point_b>=0:
        if now_a[point_a]!=0 and new_b[point_b]!=0:
            answer=max(answer,point_a+point_b)
        if now_a[point_a]>=new_b[point_b]:
            now_a[point_a]-=new_b[point_b]
            point_b-=1
        else:
            new_b[point_b]-=now_a[point_a]
            point_a+=1
    print(answer)