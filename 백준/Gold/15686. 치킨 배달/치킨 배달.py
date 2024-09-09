from itertools import combinations as cb

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

chicken = [[i,j] for i in range(n) for j in range(n) if a[i][j] == 2]
home = [[i,j] for i in range(n) for j in range(n) if a[i][j] == 1]

chi_list = list(cb(chicken, m))
def calc_dist(ho, chicken_list):
    min_dist = 1e9
    for chi in chicken_list:
        dist = abs(chi[0] - ho[0]) + abs(chi[1] - ho[1])
        min_dist = min(min_dist, dist)
    return min_dist

ans = []
for chi in chi_list:
    total = 0
    for h in home:
        total += calc_dist(h, chi)
    ans.append(total)

print(min(ans))

