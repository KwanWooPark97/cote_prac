import copy
def solution(n):
    answer = 0
    cnt=copy.deepcopy(n)
    a=bin(n)[2:].count('1')
    while True:
        cnt+=1
        b=bin(cnt)[2:].count('1')
        if a==b:
            return cnt
  