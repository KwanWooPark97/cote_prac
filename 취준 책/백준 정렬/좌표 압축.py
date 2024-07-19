import sys
n=int(input())

data=list(map(int,sys.stdin.readline().split()))

val=list(set(data))

val.sort()

dic_val={v:i for i,v in enumerate(val)}

for i in data:
    print(dic_val[i], end=' ')

