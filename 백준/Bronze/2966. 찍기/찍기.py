n=int(input())
d=list(input())

Adrian=['A','B','C']*34
Bruno=['B','A','B','C']*25
Goran=['C','C','A','A','B','B']*17
answer=[0,0,0]
for i in range(n):
    if d[i]==Adrian[i]:
        answer[0]+=1
    if d[i]==Bruno[i]:
        answer[1]+=1
    if d[i]==Goran[i]:
        answer[2]+=1

re=max(answer)
print(re)
name=['Adrian','Bruno','Goran']
for i in range(3):
    if answer[i]==re:
        print(name[i])