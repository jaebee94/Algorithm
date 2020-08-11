from itertools import combinations

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
di = [0, -1, 0]
dj = [-1, 0, 1]

def kill(archor, tmp_board, turn):
    s = [archor]
    visited = [[0]*M for _ in range(N)]
    while s:
        i, j = s.pop(0)
        if i < N:
            visited[i][j] = 1
        for k in range(3):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N-turn and 0 <= nj < M and visited[ni][nj] != 1:
                if abs(archor[0] - ni) + abs(archor[1] - nj) > D:
                    return
                elif tmp_board[ni][nj] == 1:
                    return (ni, nj)
                else:
                    s.append((ni, nj))
    return

def play(position):
    tmp_board = [enemy[:] for enemy in board]
    killed = 0
    for turn in range(N):
        kill_position = []
        for x in position:
            tmp_position = kill((N-turn, x), tmp_board, turn)
            if tmp_position != None:
                kill_position.append(tmp_position)
        for l in kill_position:
            if tmp_board[l[0]][l[1]] == 1:
                tmp_board[l[0]][l[1]] = 0
                killed += 1
    return killed


archors = [i for i in range(M)]
archor_candidates = combinations(archors, 3)

max_v = 0
for archor_candidate in archor_candidates:
    max_v = max(max_v, play(archor_candidate))

print(max_v)