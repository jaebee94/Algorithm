from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = []
q = deque()


def move(x, y, dx, dy):
    count = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count


def bfs():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                redx = i
                redy = j
            if board[i][j] == 'B':
                bluex = i
                bluey = j
    q.append([redx, redy, bluex, bluey, 1])
    visited.append([redx, redy, bluex, bluey])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        redx, redy, bluex, bluey, num = q.popleft()
        
        if num > 10:
            print(-1)
            return

        for k in range(4):
            new_redx, new_redy, count_red = move(redx, redy, dx[k], dy[k])
            new_bluex, new_bluey, count_blue = move(bluex, bluey, dx[k], dy[k])

            if board[new_bluex][new_bluey] == 'O':
                continue
            if board[new_redx][new_redy] == 'O':
                print(num)
                return
            if new_redx == new_bluex and new_redy == new_bluey:
                if count_red > count_blue:
                    new_redx -= dx[k]
                    new_redy -= dy[k]
                else:
                    new_bluex -= dx[k]
                    new_bluey -= dy[k]

            if [new_redx, new_redy, new_bluex, new_bluey] not in visited:
                q.append([new_redx, new_redy, new_bluex, new_bluey, num + 1])
                visited.append([new_redx, new_redy, new_bluex, new_bluey])

    print(-1)

bfs()
