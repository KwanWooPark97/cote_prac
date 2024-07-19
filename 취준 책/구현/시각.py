import time

N=int(input())

count=0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
print(count)

#혼자 풀려다가 보기 while 문 이용해서 한개씩 더해보려 했는데 생각해야되는 경우의수가 너무 많음
#위에 답이 제일 간단하면서도 좋은 해답같음