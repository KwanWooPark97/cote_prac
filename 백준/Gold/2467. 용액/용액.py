import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
answer=[5000000000,0,0]
start=0
end=n-1

while start<end:
    c=a[end]+a[start]
    if answer[0]>=abs(c):
        answer=[abs(c),a[start],a[end]]
        if c==0:
            break
    if c>0:
        end-=1
    else:
        start+=1

print(answer[1],answer[2])