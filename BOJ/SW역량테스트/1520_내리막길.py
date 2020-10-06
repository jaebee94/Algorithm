import sys
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    # 목적지 도착
    if x == N - 1 and y == M - 1:
        return 1
    temp = 0
    # 갔던 곳
    # if visited[x][y] != -1:
    #     return visited[x][y]
    # 0으로 초기화
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 안이면,
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] < board[x][y]:
            if visited[nx][ny] >= 0:
                temp += visited[nx][ny]
            else:
                temp += dfs(nx, ny)
    visited[x][y] = temp
    return temp

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
visited[0][0] = 0
print(dfs(0, 0))