
def dfs(i, j):
    global infinite

    if visited[i][j]:
        infinite = True
        return -1
    if cnt[i][j] != 1:
        return cnt[i][j]

    visited[i][j] = True

    for k in range(4):
        ni = i + di[k] * int(board[i][j])
        nj = j + dj[k] * int(board[i][j])
        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] != 'H':
            cnt[i][j] = max(cnt[i][j], dfs(ni, nj) + 1)
            if infinite:
                return -1
    visited[i][j] = False
    return cnt[i][j]

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

infinite = False
visited = [[False] * M for _ in range(N)]
cnt = [[1] * M for _ in range(N)]

print(dfs(0, 0))

