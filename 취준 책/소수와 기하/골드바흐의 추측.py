import math

n= int(input())

def is_prime(num):
    if num == 1:
        return False
    for j in range(2, int(math.sqrt(num)) + 1):
        if num % j == 0:
            return False
    return True

for _ in range(n):
    x=int(input())

    small,big=x//2,x//2

    while small >=1:
        if is_prime(small) and is_prime(big):
            print(small,big)
            break
        else:
            small -= 1
            big +=1
