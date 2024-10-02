import sys
n=int(sys.stdin.readline())
cow=[]
for _ in range(n):
    cow.append(list(map(int,sys.stdin.readline().split())))

cow.sort()

time=0

for i in range(n):
    if time<=cow[i][0]:
        time=cow[i][0]
    time+=cow[i][1]
print(time)