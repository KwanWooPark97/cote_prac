n=str(input())

data=list(map(int,list(n)))

data.sort(reverse=True)
result=''.join(map(str,data))
print(result)