import sys

a=int(input())

b=[]
for i in range(a):
    c=int(input())

    if c==0:
        b.pop()
    else:
        b.append(c)

print(sum(b))
