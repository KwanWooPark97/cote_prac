x=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(x)):
    for j in range(i,0,-1):
        if x[j]<x[j-1]:
            x[j],x[j-1]=x[j-1],x[j]
        else: break

print(x)