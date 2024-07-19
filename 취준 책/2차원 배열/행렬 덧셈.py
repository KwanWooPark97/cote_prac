n,m=map(int,input().split())

data1=[]
data2=[]
for _ in range(n):
    a=list(map(int,input().split()))
    data1.append(a)

for _ in range(n):
    b=list(map(int,input().split()))
    data2.append(b)

for i in range(n):
    for j in range(m):
        print(data1[i][j]+data2[i][j],end=' ')
    print()