import sys

n=int(input())

data={}
for _ in range(n):
    x,y=map(int,sys.stdin.readline().split())
    if y not in data:
        data[y]=[x]
    else:
        data[y].append(x)

key_list=list(data.keys())

key_list.sort()

for key in key_list:
    val=data[key]
    if len(val) >=2:
        val.sort()

    for i in range(len(val)):
        print(val[i],key)


