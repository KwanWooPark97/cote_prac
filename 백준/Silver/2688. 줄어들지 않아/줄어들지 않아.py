t=int(input())

def dfs(s):
    if len(s)==n:
        global answer
        answer+=1
        return

    for i in range(int(s[-1]),10):
        dfs(s+str(i))

for _ in range(t):
    answer = 0
    n=int(input())
    '''for i in range(10):
        dfs(str(i))
    print(answer)'''
    new_dp=[]
    dp=[10,9,8,7,6,5,4,3,2,1]
    for i in range(1,n):
        for i in range(10):
            new_dp.append(sum(dp))
            dp.pop(0)
        dp=new_dp
        new_dp=[]
    print(dp[0])