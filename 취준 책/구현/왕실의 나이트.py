import time

data=input()

row=int(data[1])

col=int(ord(data[0])-ord('a'))+1

move=[(-2,-1),(-2,+1),(2,-1),(2,+1),(-1,-2),(-1,+2),(1,-2),(1,2)]

count=0


for move in move:
    new_row= row +move[0]
    new_col= col +move[1]

    if new_col<=0 or new_row <=0 or new_row >8 or new_col >8:
        continue

    count+=1

print(count)
