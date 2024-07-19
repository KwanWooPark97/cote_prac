
x=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(x)):
    small_index=i
    for j in range(i+1,len(x)):
        if x[small_index] > x[j]:
            small_index=j

    x[i],x[small_index]=x[small_index],x[i]

print(x)            