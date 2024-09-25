from itertools import combinations as cb

team=list(map(int,input().split()))

team.sort()

print(abs((team[0]+team[-1])-(team[1]+team[2])))


