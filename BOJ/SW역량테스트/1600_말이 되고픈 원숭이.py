from collections import deque

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

hi = [1, 2, 2, 1, -1, -2, -2, -1]
hj = [2, 1, -1, -2, -2, -1, 1, 2]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

q = deque()
q.append((0, 0, 0))
visited = [(0, 0, 0)]
cnt = 0
result = False
while q:
    x, y, t = q.popleft()
    if x == H-1 and y == W-1:
        result = t
        break
    if t < K:
        for a in range(8):
            ni = x + hi[a]
            nj = y + hj[a]
            if 0 <= ni < H and 0 <= nj < W and board[ni][nj] != 1 and (ni, nj) not in visited:
                visited.append((ni, nj))
                q.append((ni, nj, t + 1))
        for b in range(4):
            ni = x + di[b]
            nj = y + dj[b]
            if 0 <= ni < H and 0 <= nj < W and board[ni][nj] != 1 and (ni, nj) not in visited:
                visited.append((ni, nj))
                q.append((ni, nj, t + 1))
    else:
        for b in range(4):
            ni = x + di[b]
            nj = y + dj[b]
            if 0 <= ni < H and 0 <= nj < W and board[ni][nj] != 1 and (ni, nj) not in visited:
                visited.append((ni, nj))
                q.append((ni, nj, t + 1))
if result:
    print(result)
else:
    print(-1)