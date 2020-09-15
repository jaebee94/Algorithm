import collections
import pprint

def bfs(i, j, h):
    q = collections.deque()
    now = [i, j]
    supply = [now]
    q.append(now)
    visited[i][j] = True
    flag = False
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and board[ni][nj] != 0:
                if visited[ni][nj] == False and board[ni][nj] < h:
                    visited[ni][nj] = True
                    print(h, 'visited', ni, nj)
                    pprint.pprint(visited)
                    supply.append([ni, nj])
                    q.append([ni, nj])
            else:
                flag = True
    if flag:
        return 0
    water = 0
    for point in supply:
        board[point[0]][point[1]] += 1
        water += 1
    return water

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

maxH = 0
answer = 0
for i in range(N):
    maxH = max(maxH, max(board[i]))

for h in range(1, maxH+1):
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] and board[i][j] < h and visited[i][j] == False:
                answer += bfs(i, j, h)
print(answer)