
result=1

def fact(n):
    global result
    result *=n
    if (n-1)==1:
        return result

    fact(n-1)

fact(4)

print(result)
