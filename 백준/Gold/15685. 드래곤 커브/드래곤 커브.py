import copy
n=int(input())

final=[]

def rotate(g,news):
    for i in range(g):
        a, b = news[-1]
        for nx,ny in news[:-1][::-1]:
            new_x=(ny-b)+a
            new_y=-(nx-a)+b
            news.append([new_x,new_y])
    return news
for i in range(n):
    new=[]
    x,y,d,g=map(int,input().split())
    new.append([x,-y])
    if d==0:
        new.append([x+1,-y])
    elif d==1:
        new.append([x,-y+1])
    elif d==2:
        new.append([x-1,-y])
    elif d==3:
        new.append([x,-y-1])
    final.extend(rotate(g,copy.deepcopy(new)))

final=list(set(map(tuple,final)))
answer=0
for x,y in final:
    if (x+1,y-1) in final and (x+1,y) in final and (x,y-1) in final:
        answer+=1
print(answer)
