import copy
from collections import deque
n=int(input())
pa=input().split('*')

for i in range(n):
    s=input()
    if len(pa[0]+pa[1])>len(s):
        print('NE')
    #print(s[:len(pa[0])],s[len(s)-len(pa[1]):])
    elif s[:len(pa[0])]==pa[0] and s[len(s)-len(pa[1]):]==pa[1]:
        print('DA')
    else:
        print('NE')


