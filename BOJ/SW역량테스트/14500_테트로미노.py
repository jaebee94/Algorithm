N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
blocks = [
    [(0, 1), (1, 0), (1, 1)],
    [(0, 1), (0, 2), (0, 3)],
    [(1, 0), (2, 0), (3, 0)],
    [(0, 1), (0, 2), (1, 0)],
    [(0, 1), (0, 2), (-1, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(0, 1), (0, 2), (1, 2)],
    [(1, 0), (2, 0), (2, 1)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 1), (1, 0), (2, 0)],
    [(1, 0), (2, 0), (2, -1)],
    [(1, 0), (1, 1), (2, 1)],
    [(0, 1), (1, 0), (-1, 1)],
    [(0, 1), (1, 0), (1, -1)],
    [(0, 1), (1, 1), (1, 2)],
    [(0, 1), (0, 2), (1, 1)],
    [(1, 0), (1, 1), (1, -1)],
    [(1, 0), (2, 0), (1, -1)],
    [(1, 0), (1, 1), (2, 0)]
]
answer = 0

for i in range(N):
    for j in range(M):
        for x in range(19):
            start = board[i][j]
            for y in range(3):
                try:
                    ni = i + blocks[x][y][0]
                    nj = j + blocks[x][y][1]
                    start += board[ni][nj]
                except IndexError:
                    break
            answer = max(answer, start)
print(answer)