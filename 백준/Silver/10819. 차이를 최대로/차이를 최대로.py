import sys
import itertools
n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))

max_v=0
a=list(itertools.permutations(nums,n))
for i in a:
    re=0
    for j in range(len(i)-1):
        re+=abs(i[j]-i[j+1])
    max_v=max(re,max_v)

print(max_v)



