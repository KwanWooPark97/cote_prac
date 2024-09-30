import sys
n=int(sys.stdin.readline().rstrip())

cnt=0

while True:
    if n<10:
        print(cnt)
        if n%3==0:
            print('YES')
        else:
            print('NO')
        break
    new=0
    for i in str(n):
        new+=int(i)
    #n=sum(list(map(int,list(str(n)))))
    n=new
    cnt+=1