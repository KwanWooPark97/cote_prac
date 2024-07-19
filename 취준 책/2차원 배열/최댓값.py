
max_val=0
save_i=0
save_j=0
for i in range(9):
    data=list(map(int,input().split()))

    if max(data)>max_val:
        max_val=max(data)
        save_i=i
        save_j=data.index(max_val)

print(max_val)
print(save_i+1,save_j+1)