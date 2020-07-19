dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
board = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    board[x][y] = 1
    move = [d]
    for _ in range(g):
        temp = []
        for i in range(len(move)):
            temp.append((move[-i-1] + 1) % 4)
        move.extend(temp)
    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        board[nx][ny] = 1
        x, y = nx, ny

ans = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and  board[i][j+1] and  board[i+1][j+1]:
            ans += 1
print(ans)
