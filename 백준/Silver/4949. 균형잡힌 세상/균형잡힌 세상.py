import sys

while True:
    b = []
    suc=0
    c=list(map(str,sys.stdin.readline().rstrip()))
    if c[0]=='.':
        break
    for i in c:
        if i=='(' or i=='[':
            b.append(i)

        if len(b)==0 and (i==')' or i==']'):
            print('no')
            suc=1
            break

        if i==')':
            d=b.pop()
            if d != '(':
                print('no')
                suc=1
                break
        elif i==']':
            d = b.pop()
            if d != '[':
                print('no')
                suc=1
                break

    if len(b)==0 and suc==0:
        print("yes")
    elif len(b)!=0 and suc==0:
        print("no")