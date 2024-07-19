data=[0,1]

def fibonachi(n):
    if n==1 or n==0:
        return
    else:
        data.append(data[-2]+data[-1])
        return fibonachi(n-1)

a=int(input())
fibonachi(a)

if a==0:
    print(data[0])
else:
    print(data[-1])