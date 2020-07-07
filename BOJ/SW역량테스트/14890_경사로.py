n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
vertical_board = list(map(list, list(zip(*board))))

def solution(n, l, board):
    cnt = 0
    for i in range(n):
        continuous = 0
        pre_height = -1
        cur_height = -1
        checked = False

        for j in range(n):
            cur_height = board[i][j]

            if pre_height >= 0 and pre_height != cur_height:
                if checked:
                    if l == continuous:
                        continuous = 1
                        checked = False
                        continue
                    else:
                        break

                gap = pre_height - cur_height

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

            pre_height = cur_height

        else:
            if not checked:
                cnt += 1
    return cnt

print(solution(n, l, board) + solution(n, l, vertical_board))