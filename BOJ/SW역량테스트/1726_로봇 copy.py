from collections import deque

M, N = map(int, input().split())
status = [list(map(int, input().split())) for _ in range(M)]
start_x, start_y, start_d = map(int, input().split())
final_x, final_y, final_d = map(int, input().split())

# visited = [[False] * N for _ in range(M)]
visited = []
# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = {
    1: 0,
    2: 2,
    3: 1,
    4: 3
}
start_d = direction[start_d]
final_d = direction[final_d]


def bfs(x, y, d):
    def rotate(x, y, d, c):
        for k in range(4):
            if d + k >= 4:
                nd -= 4
            else:
                nd = d + k
            nx = x + dx[nd]
            ny = y + dy[nd]
            if k == 3:
                temp = 1
            else:
                temp = k
            if 0 <= nx < M and 0 <= ny < N and status[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx, ny, nd, c + temp))
    q = deque()
    q.append((x, y, d, 0))
    visited[x][y] = True
    visited.append((x, y, d))
    minV = 10000000

    while q:
        x, y, d, c = q.popleft()
        if x == final_x - 1 and y == final_y - 1:
            temp = abs(d - final_d)
            if temp == 3:
                temp = 1
            minV =  c + temp
            for x, y, d, c in q:
                if x == final_x - 1 and y == final_y - 1:
                    temp = abs(d - final_d)
                    if temp == 3:
                        temp = 1
                    minV = min(minV, c + temp)
            return minV

        
                for i in range(1, 4):
                    nx = x + dx[k] * i
                    ny = y + dy[k] * i
                    # print('후보', nx, ny)
                    if 0 <= nx < M and 0 <= ny < N and status[nx][ny] == 0 and (nx, ny, k+1) not in visited:
                        # visited[nx][ny] = True
                        visited.append((nx, ny, k+1))
                        q.append((nx, ny, k + 1, c + temp + 1))
                    # if nx == final_x - 1 and ny == final_y - 1:
                        # visited[nx][ny] = False

print(bfs(start_x-1, start_y-1, start_d))
