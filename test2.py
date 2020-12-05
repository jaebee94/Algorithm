def solution(board, K, Ax, Ay):
    N = len(board)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    bomb = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                bomb[i][j] = True
                for k in range(4):
                    for l in range(1, K + 1):
                        ni = i + di[k] * l
                        nj = j + dj[k] * l
                        if 0 <= ni < N and 0 <= nj < N:
                            if board[ni][nj] == 2:
                                break
                            elif not bomb[ni][nj]:
                                bomb[ni][nj] = True
                        else:
                            break

    s = [(Ax, Ay, 0)]
    visit = [[False] * N for _ in range(N)]
    while s:
        i, j, t = s.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if not bomb[ni][nj] and board[ni][nj] != 2:
                    return t + 1
                if bomb[ni][nj] and board[ni][nj] == 0 and not visit[ni][nj]:
                    visit[ni][nj] = True
                    s.append((ni, nj, t+1))
    return -1

board1 = [[0, 0, 1, 0, 0, 0], [0, 2, 0, 0, 0, 1], [0, 0, 2, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0]]
K1, Ax1, Ay1 = 2, 1, 2
board2 = [[0, 0, 0, 1], [0, 2, 0, 1], [2, 0, 0, 1], [1, 2, 0, 1]]
K2, Ax2, Ay2 = 2, 2, 1
print(solution(board1, K1, Ax1, Ay1))
print(solution(board2, K2, Ax2, Ay2))