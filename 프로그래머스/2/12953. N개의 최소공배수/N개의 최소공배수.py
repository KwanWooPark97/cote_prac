def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    g=gcd(a,b)
    return a*b//g
    
def solution(arr):
    answer = 0
    a=arr[0]
    for i in range(1,len(arr)):
        a=lcm(arr[i],a)
            
    return a