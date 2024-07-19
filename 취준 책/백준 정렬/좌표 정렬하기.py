import sys

n=int(input())

data={}
for _ in range(n):
    x,y=map(int,sys.stdin.readline().split())
    if x not in data:
        data[x]=[y]
    else:
        data[x].append(y)

key_list=list(data.keys())

key_list.sort()

for key in key_list:
    val=data[key]
    if len(val) >=2:
        val.sort()

    for i in range(len(val)):
        print(key,val[i])


