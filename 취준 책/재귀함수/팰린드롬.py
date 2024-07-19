
def recursion(s, l, r,count):
    count +=1
    if l >= r: return 1,count
    elif s[l] != s[r]: return 0,count
    else: return recursion(s, l+1, r-1,count)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1,0)


t=int(input())

for _ in range(t):
    s=input()
    val,count=isPalindrome(s)
    print(val,count)

