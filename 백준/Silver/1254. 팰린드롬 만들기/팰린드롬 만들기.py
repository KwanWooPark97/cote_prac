import copy
from collections import deque
s=input()

for i in range(len(s)):
    p=s[i:]

    if p==p[::-1]:
        print(len(s)+i)
        break