from collections import deque

M, N = map(int, input().split())
status = [list(map(int, input().split())) for _ in range(M)]
start_x, start_y, start_d = map(int, input().split())
final_x, final_y, final_d = map(int, input().split())

visited = [[[False] * 4 for _ in range(N)] for _ in range(M)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, d):
    q = deque()
    q.append((x, y, d, 0))
    while q:
        x, y, d, c = q.popleft()
        if x == final_x - 1 and y == final_y - 1 and d == final_d-1:
            print(c)
            return
        for i in range(1, 4):
            nx = x + dx[d] * i
            ny = y + dy[d] * i
            if 0 <= nx < M and 0 <= ny < N and status[nx][ny] != 0:
                break
            if 0 <= nx < M and 0 <= ny < N and status[nx][ny] == 0 and not visited[nx][ny][d]:
                q.append((nx, ny, d, c + 1))
                visited[nx][ny][d] = True

        for i in range(4):
            if i == d:
                continue
            k = 2 if (i+d)%4 == 1 else 1
            if not visited[x][y][i]:
                q.append((x, y, i, c + k))
                visited[x][y][i] = True

bfs(start_x-1, start_y-1, start_d-1)
