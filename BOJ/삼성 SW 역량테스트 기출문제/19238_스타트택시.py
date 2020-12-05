from collections import deque

N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
start_x, start_y = map(int, input().split())
start_x -= 1
start_y -= 1
num = 2
for _ in range(M):
    p1, p2, g1, g2 = map(int, input().split())
    board[p1-1][p2-1] = num
    board[g1-1][g2-1] = 'g' + str(num)
    num += 1

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
passenger = False
success = True

used = 0
while num > 2:
    visit = [[False] * N for _ in range(N)]
    q = deque()
    q.append((start_x, start_y, fuel, used))
    print('find')
    while q:
        i, j, fuel, used = q.popleft()
        print(i, j, fuel, used)
        if not passenger:
            if type(board[i][j]) == int and board[i][j] > 1:
                passenger = True
                start_x, start_y = i, j
                goal = board[i][j]
                board[i][j] = 0
                print('passenger')
                break
        else:
            if type(board[i][j]) == str and board[i][j] == 'g' + str(goal):
                passenger = False
                start_x, start_y = i, j
                board[i][j] = 0
                num -= 1
                fuel += used * 2
                used = 0
                print('goal')
                break
        if fuel <= 0:
            success = False
            break
        visit[i][j] = True
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj] and board[ni][nj] != 1:
                if passenger:
                    q.append((ni, nj, fuel - 1, used + 1))
                else:
                    q.append((ni, nj, fuel - 1, 0))
                visit[ni][nj] = True
    if not success:
        break

if success:
    print(fuel)
else:
    print(-1)
