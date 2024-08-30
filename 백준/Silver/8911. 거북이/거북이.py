n=int(input())

for _ in range(n):
    p_x=[0]
    p_y=[0]
    d=1
    x,y=0,0
    m=list(input())
    for i in m:
        if i=='L':
            d=(d-1)%4
        elif i=='R':
            d=(d+1)%4
        elif i=='F':
            if d==0:
                x-=1
            elif d==1:
                y+=1
            elif d==2:
                x+=1
            elif d==3:
                y-=1
            p_x.append(x)
            p_y.append(y)
        elif i=='B':
            if d==0:
                x+=1
            elif d==1:
                y-=1
            elif d==2:
                x-=1
            elif d==3:
                y+=1
            p_x.append(x)
            p_y.append(y)
    print((max(p_x)-min(p_x))*(max(p_y)-min(p_y)))


