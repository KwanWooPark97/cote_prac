p,w=map(int,input().split())

r=input()

num=[2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
cnt=[1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,4,1,2,3,1,2,3,4]
answer=0
for i in range(len(r)):
    if r[i]==' ':
        answer+=p
        continue
    c=ord(r[i])-ord('A')
    if i>0 and r[i-1]!= ' ' and num[c]==num[ord(r[i-1])-ord('A')]:
        answer+=w
    answer+=cnt[c]*p
print(answer)
