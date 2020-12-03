import copy
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
virus_list = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus_list.append([i, j])


def virus(virus_map):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for v in virus_list:
        q = deque()
        q.append(v)
        while q:
            i, j = q.popleft()
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if virus_map[ni][nj] == 0:
                        virus_map[ni][nj] = 2
                        q.append([ni, nj])
    cnt = 0
    for i in range(N):
        for j in range(M):
            if virus_map[i][j] == 0:
                cnt += 1
    return cnt


def wall(x):
    global answer
    if x == 3:
        virus_map = copy.deepcopy(board)
        answer = max(answer, virus(virus_map))
        return
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(x+1)
                board[i][j] = 0


wall(0)
print(answer)
