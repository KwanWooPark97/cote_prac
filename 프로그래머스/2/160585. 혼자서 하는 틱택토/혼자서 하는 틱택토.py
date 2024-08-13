import copy
def solution(board):
    answer = -1
    method = []

    def check_row(bo,now):
        for k in range(3):
            if bo[k].count(now) == 3:
                return True
        return False

    def check_col(bo,now):
        for k in range(3):
            if bo[0][k] == bo[1][k] == bo[2][k] ==now:
                return True
        return False

    def check_in(bo,now):
        if (bo[0][0] == bo[1][1] == bo[2][2] == now) or (bo[2][0] == bo[1][1] == bo[0][2] == now):
            return True
        return False

    def done(bo):
        for i in range(3):
            for j in range(3):
                if bo[i][j] == '.':
                    return False
        return True

    bo = [list(row) for row in board]

    o_count, x_count = 0, 0
    for row in bo:
        for c in row:
            if c == 'O':
                o_count += 1
            if c == 'X':
                x_count += 1

    if not (o_count == x_count or o_count == x_count + 1):
        return 0

    if (check_row(bo,'O') or check_col(bo,'O') or check_in(bo,'O')) and (check_row(bo,'X') or check_col(bo,'X') or check_in(bo,'X')):
        return 0
    
    if (check_row(bo,'O') or check_col(bo,'O') or check_in(bo,'O')) and o_count != x_count + 1:
        return 0
    
    if (check_row(bo,'X') or check_col(bo,'X') or check_in(bo,'X')) and o_count != x_count:
        return 0

    return 1
