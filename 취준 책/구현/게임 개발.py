import time

n,m=map(int,input().split())

a,b,way=map(int,input().split())

gmap=[]
exp=[]
result=1
for _ in range(4):
    data=list(map(int,input().split()))
    gmap.append((data))

move_type=[(-1,0),(0,-1),(1,0),(0,1)]
back_move=[(0,1),(-1,0),(0,-1),(1,0)]
exp.append([a,b])
nway=way
while True:
    new_b=b+move_type[nway][0]
    new_a=a+move_type[nway][1]

    if gmap[new_a][new_b]==1:
        nway=(nway+1)%4
        if nway==way:
            new_b=b+back_move[nway][0]
            new_a=a+back_move[nway][1]
            if gmap[new_a][new_b]==1:
                break
        continue
    elif exp==[new_a,new_b]:
        nway = (nway + 1) % 4
        continue
    elif gmap[new_a][new_b]==0:
        b=new_b
        a=new_a
        result +=1
        exp.append([new_a,new_b])

print(result)

#이것도 답이 되는거 같음 입력값을 토대로 하면 정답이 나옴