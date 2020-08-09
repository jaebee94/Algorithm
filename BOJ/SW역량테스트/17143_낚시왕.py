def move():
    temp = [[0] * C for i in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0:
                x, y, s, d, z = i, j, board[i][j][0], board[i][j][1], board[i][j][2]
                while s > 0:
                    x += dx[d]
                    y += dy[d]
                    if 0 <= x < R and 0 <= y < C:
                        s -= 1
                    else:
                        x -= dx[d]
                        y -= dy[d]
                        if d == 0:
                            d = 1
                        elif d == 1:
                            d = 0
                        elif d == 2:
                            d = 3
                        else:
                            d = 2
                if temp[x][y] == 0:
                    temp[x][y] = [board[i][j][0], d, z]
                else:
                    if temp[x][y][2] < z:
                        temp[x][y] = [board[i][j][0], d, z]
    return temp


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
R, C, M = map(int, input().split())
board = [[0] * C for i in range(R)]
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r - 1][c - 1] = [s, d - 1, z]

result = 0
for j in range(C):
    for i in range(R):
        if board[i][j] != 0:
            result += board[i][j][2]
            board[i][j] = 0
            break
    board = move()
print(result)