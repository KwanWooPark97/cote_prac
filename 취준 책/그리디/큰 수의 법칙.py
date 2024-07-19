import time



n, m, k=map(int, input().split())

data=list(map(int,input().split()))
start_time=time.time()
result=0
epoch=1
data.sort() #데이터 큰수로 정렬

for _ in range(m):
    if epoch%k==0:
        result += data[n-2]
    else:
        result += data[n-1]
    epoch +=1

end_time=time.time()
fps=end_time-start_time
print(result,round(end_time-start_time,10))

#책 정답

result =0
start_time=time.time()
first=data[n-1]#가장 큰 수
second=data[n-2]#가장 작은 수

while True:
    for i in range(k):
        if m ==0 :
            break
        result += first
        m -=1
    if m==0 :
        break
    result += second
    m-=1
end_time=time.time()
print(result,round(end_time-start_time,10))

#위의 방법들은 N이 커지면 시간 초과 가능성도 있음

count= m//(k+1)*k#가장 큰수가 곱해지는 횟수 k+1은 k번 큰 수가 더해지고 1번은 두번째 수가 더해진다. 따라서 count
count += m%(k+1)# 나머지 큰수가 더해지는 횟수

result=0

result += first*count
result += (m-count)*second