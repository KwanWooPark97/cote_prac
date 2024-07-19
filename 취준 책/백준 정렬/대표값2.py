import math
data=[]
for i in range(5):
    n=int(input())

    data.append(n)
data.sort()

print(int(sum(data)/len(data)))
print(data[2])
