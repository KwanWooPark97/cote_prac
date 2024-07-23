from collections import Counter,deque
num=list(input())

a=Counter(num)

zero=a['0']//2
one=a['1']//2
for i in range(one):
    num.remove('1')
num=num[::-1]
for j in range(zero):
    num.remove('0')

print(''.join(num[::-1]))
