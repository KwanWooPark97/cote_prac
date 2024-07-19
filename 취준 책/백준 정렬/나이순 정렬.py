import sys
n=int(input())


data={}
for _ in range(n):
    age,name=sys.stdin.readline().split()

    if age not in data.keys():
        data[age]=[name]
    else:
        data[age].append(name)

key_list = list(map(int,data.keys()))

key_list.sort()

key_list=list(map(str,key_list))
for key in key_list:
    val = list(data[key])
    for i in range(len(val)):
        print(int(key),str(val[i]))