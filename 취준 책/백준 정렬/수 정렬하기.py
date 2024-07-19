n=int(input())

data=[]
for _ in range(n):
    m=int(input())

    data.append(m)

data.sort()
for i in range(len(data)):
    print(data[i])

