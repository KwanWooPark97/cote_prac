import sys

input = lambda: sys.stdin.readline().rstrip()
def move_balls(type_of_ball_to_move,s):
    s=s.lstrip(type_of_ball_to_move)
    return s.count(type_of_ball_to_move)

n = int(input())
s=input()
print(min(
    move_balls("R",s), #빨간색 왼쪽으로
    move_balls("R",s[::-1]),#빨간색 오른쪽으로
    move_balls("B",s),#파란색 왼쪽으로
    move_balls("B",s[::-1])))#파란색 오른쪽으로