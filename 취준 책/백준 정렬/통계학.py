import sys
n=int(input())

data=[]
for _ in range(n):
    data.append(int(sys.stdin.readline()))
data.sort()

mean=round(sum(data)/len(data))

middle_val=data[n//2]

dic= {}

for i in data:
    if i not in dic:
        dic[i] =1
    else:
        dic[i]=dic[i]+1

max_val=max(dic.values())
vin_val=[]
for key,val in dic.items():
    if val ==max_val:
        vin_val.append(int(key))

range_val=data[-1]-data[0]

if len(vin_val) >=2:
    vin=vin_val[1]
else:
    vin=vin_val[0]

print(mean)
print(middle_val)
print(vin)
print(range_val)


