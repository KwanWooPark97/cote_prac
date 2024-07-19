import sys

n = int(input())
num = [0 for _ in range(10001)]

for _ in range(n):
    a=int(sys.stdin.readline())
    num[a] +=1


for i in range(len(num)):
    if num[i] != 0:
        for _ in range(num[i]):
            print(i)