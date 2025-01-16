n=int(input())
ch=[]

for _ in range(n):
    ch.append(input().rstrip())

cursor=0
answer=''
while True:
    if ch[cursor]=='KBS1':
        ch.remove('KBS1')
        ch.insert(0,'KBS1')
        answer+='4'*cursor
        cursor=0
        break
    else:
        answer+='1'
        cursor+=1
#print(ch)
while True:
    if ch[cursor]=='KBS2':
        answer+='4'*(cursor-1)
        break
    else:
        answer+='1'
        cursor+=1
print(answer)

