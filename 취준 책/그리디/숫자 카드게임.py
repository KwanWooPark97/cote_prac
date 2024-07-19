import time

n,m=map(int,input().split())
minvalue=0

for i in range(n):
    data=list(map(int,input().split()))
    min_value=min(data)
    if i==0:
        result=min_value
    else:
        result=max(min_value,result)
end_time=time.time()
print(result)

#정답이랑 같음