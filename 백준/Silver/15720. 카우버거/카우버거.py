b,c,d=map(int,input().split())

ham=list(map(int,input().split()))
side=list(map(int,input().split()))
ber=list(map(int,input().split()))

ori=sum(ham)+sum(side)+sum(ber)
ham.sort()
side.sort()
ber.sort()

t=min(b,c,d)
answer=0
for i in range(t):
    answer+=(ham.pop()+side.pop()+ber.pop())*0.9

answer+=sum(ham)+sum(side)+sum(ber)

print(ori)
print(int(answer))