n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
vertical_board = list(map(list, list(zip(*board))))

def solution(n, l, board):
    cnt = 0
    for i in range(n):
        continuous = 0
        pre_h = -1
        cur_h = -1
        checked = False

        for j in range(n):
            cur_h = board[i][j]

            if pre_h >= 0 and pre_h != cur_h:
                if checked:
                    if l == continuous:
                        continuous = 1
                        checked = False
                        continue
                    else:
                        break

                gap = pre_h - cur_h

                if abs(gap) != 1:
                    break
                    
                if gap < 0:
                    if l <= continuous:
                        continuous = 1
                    else:
                        break
                else:
                    continuous = 1
                    checked = True
                    if l == continuous:
                        continuous = 0
                        checked = False
            else:
                continuous += 1
                if checked:
                    if l == continuous:
                        continuous = 0
                        checked = False

            pre_h = cur_h

        else:
            if not checked:
                cnt += 1
    return cnt

print(solution(n, l, board) + solution(n, l, vertical_board))