n=int(input())

a=list(map(int,input().split()))
c=[i for i in range(1,n+1)]
c=c[::-1]
a=a[::-1]

answer=[]

for idx,val in zip(a,c):
    answer.insert(idx,val)
for i in answer:
    print(i,end=' ')