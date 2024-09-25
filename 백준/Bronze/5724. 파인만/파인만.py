dp=[1,5]

for i in range(3,101):
    dp.append(i**2+dp[i-2])

while True:
    n=int(input())
    if n==0:
        break
    print(dp[n-1])
