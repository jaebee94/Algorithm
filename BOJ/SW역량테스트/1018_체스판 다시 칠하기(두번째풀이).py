N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
minV = 64
for i in range(N - 7):
    for j in range(M - 7):
        change_W = 0
        change_B = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if board[x][y] != 'W':
                        change_W += 1
                    else:
                        change_B += 1
                else:
                    if board[x][y] != 'B':
                        change_W += 1
                    else:
                        change_B += 1
        minV = min(minV, change_W, change_B)
print(minV)
