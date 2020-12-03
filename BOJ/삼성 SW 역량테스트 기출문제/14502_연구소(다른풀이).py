import copy
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
virus_list = []
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus_list.append([i, j])


def virus(virus_map, i, j):
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if virus_map[ni][nj] == 0:
                virus_map[ni][nj] = 2
                virus(virus_map, ni, nj)
    return


def wall(s, x):
    global answer

    if x == 3:
        virus_map = copy.deepcopy(board)
        for v in virus_list:
            virus(virus_map, v[0], v[1])
        answer = max(answer, sum(i.count(0) for i in virus_map))
        return

    for i in range(s, N*M):
        r = i // M
        c = i % M
        if board[r][c] == 0:
            board[r][c] = 1
            wall(i, x + 1)
            board[r][c] = 0


wall(0, 0)
print(answer)
