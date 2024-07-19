n=int(input())

paper=[[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    x,y=map(int,input().split())

    for i in range(90-y,100-y):
        for j in range(90-x,100-x):
            if paper[i][j] == 0:
                paper[i][j]=1

sum_val=0
for i in range(100):
    sum_val += sum(paper[i])
print(sum_val)