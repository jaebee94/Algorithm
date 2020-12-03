N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 2
L = int(input())
s = [list(input().split()) for _ in range(L)]

head_x, head_y = 0, 0
k = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
t = 0

snake = [(0, 0)]
board[0][0] = 1
X, C = s.pop(0)
X = int(X)
while True:
    t += 1
    head_x += dx[k]
    head_y += dy[k]
    if head_x < 0 or head_x >= N or head_y < 0 or head_y >= N or board[head_x][head_y] == 1:
        break
    elif board[head_x][head_y] == 2:
        board[head_x][head_y] = 1
        snake.append([head_x, head_y])
    else:
        board[head_x][head_y] = 1
        snake.append([head_x, head_y])
        tail_x, tail_y = snake.pop(0)
        board[tail_x][tail_y] = 0
    if t == X:
        if C == 'D':
            k = (k + 1) % 4
        else:
            k = (k + 3) % 4
        if s:
            X, C = s.pop(0)
            X = int(X)
print(t)