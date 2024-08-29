n=int(input())

adj=[[0,0,0,0,0] for _ in range(n+1)]


adj[1]=[1,1,1,1,1]

for i in range(2,n+1):
    adj[i][0]=(adj[i-1][1]+adj[i-1][2]+adj[i-1][3]+adj[i-1][4])%1000000007
    adj[i][1]=(adj[i-1][0]+adj[i-1][3]+adj[i-1][4])%1000000007
    adj[i][2]=(adj[i-1][0]+adj[i-1][4])%1000000007
    adj[i][3]=(adj[i-1][0]+adj[i-1][1])%1000000007
    adj[i][4]=(adj[i-1][0]+adj[i-1][1]+adj[i-1][2])%1000000007


print(sum(adj[n])%1000000007)