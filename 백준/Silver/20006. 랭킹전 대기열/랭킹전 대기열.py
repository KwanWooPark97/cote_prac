import sys
p,m=map(int,sys.stdin.readline().split())
room=[]
for _ in range(p):
    lev,name=sys.stdin.readline().rstrip().split()
    lev=int(lev)
    if len(room)==0:
        room.append([[lev,name]])
        continue
    for i in room:
        if i[0][0]-10<=lev<=i[0][0]+10 and len(i)<m:
            i.append([lev,name])
            break
    else:
        room.append([[lev,name]])

for i in room:
    if len(i)==m:
        print('Started!')
    else:
        print('Waiting!')
    i.sort(key=lambda x: x[1])
    for j in i:
        print(j[0],j[1])
