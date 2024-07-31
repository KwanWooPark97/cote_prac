from itertools import combinations
keys=[]

for _ in range(9):
    keys.append(int(input()))

a=combinations(keys,7)

for i in a:
    if sum(i)==100:
        k=sorted(list(i))
        for j in k:
            print(j)
        break

