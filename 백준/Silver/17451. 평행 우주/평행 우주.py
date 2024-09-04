n=int(input())

h=list(map(int,input().split()))
answer=h[-1]
for i in h[::-1]:
    if answer%i==0:
        continue

    if answer<i:
        answer=i
    else:
        answer=((answer//i)+1)*i

print(answer)