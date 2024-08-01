import sys
n,k,b=map(int,sys.stdin.readline().split())

r=[1]*n

for i in range(b):
    a=int(sys.stdin.readline())
    r[a-1]=0
psum=[r[0]]
for i in range(1,n):
    psum.append(psum[i-1]+r[i])

answer=[]
for i in range(k,len(psum)):
    answer.append(psum[i]-psum[i-k])

print(k-max(answer))
