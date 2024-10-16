import sys
n=int(sys.stdin.readline())

board=[]
for _ in range(n):
    board.append(int(sys.stdin.readline()))

dp=[0]*n#이전거 안먹음
dp[0]=board[0]
if n>=2:
    dp[1]=max(board[0]+board[1]//2,board[1])
if n>=3:
    dp[2]=max(dp[1],board[1]+board[2]//2,board[0]+board[2])

for i in range(3,n):
    dp[i] = max(dp[i - 1], dp[i - 2] + board[i], dp[i - 3] + board[i] // 2 + board[i - 1])

print(dp[n-1])
'''
dp[i]=max(dp[i-1],dp[i-2]+arr[i],dp[i-3]+arr[i]//2+arr[i-1])
'''


