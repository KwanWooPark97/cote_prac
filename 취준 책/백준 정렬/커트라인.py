n,k=map(int,input().split())

x=list(map(int,input().split()))

x.sort()
x.reverse()

print(x[k-1])