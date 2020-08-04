def bfs(l):
    global state, location, size, eat, sec
    dq = deque()
    dq.append(l)
    distance = [[-1] * N for _ in range(N)]
    distance[l[0]][l[1]] = 0
    minD = N ** 2

    while dq:
        i, j = dq.popleft()
        # 4방향 탐색
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 범위 안이고, 방문하지 않았고, 지금 크기보다 같거나 작으면
            if 0 <= ni < N and 0 <= nj < N and distance[ni][nj] == -1 and state[ni][nj] <= size:
                # 현재거리 +1 로 방문 처리, 거리 표시
                distance[ni][nj] = distance[i][j] + 1
                # 갈 수 있는 후보에 append
                dq.append([ni, nj])
                # 지금 크기보다 작으면 ( 먹을 수 있는 고기 인 경우 )
                if 0 < state[ni][nj] < size:
                    minD = min(minD, distance[ni][nj])

    next_location = []
    for i in range(N):
        for j in range(N):
            # 전체를 탐색했을 때 먹을 수 있는 고기를 찾으면
            if distance[i][j] == minD and 0 < state[i][j] < size:
                # 이동시킬 위치에 append
                next_location.append([i, j])
    # 먹을 수 있는 고기가 있으면 위, 왼, 오, 아 순으로 이동시키고 먹은 횟수 += 1, 시간 카운트
    if next_location:
        next_location.sort(key=lambda x:(x[0],x[1]))
        location = next_location[0]
        eat += 1
        sec += minD
        state[location[0]][location[1]] = 0
        return True
    else:
        return False


from collections import deque

N = int(input())
state = [list(map(int, input().split())) for _ in range(N)]

# 위, 왼, 오, 아
di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]
size = 2
eat = 0

# 아기 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if state[i][j] == 9:
            # 위치 저장하고 0으로 바꾸기
            location = [i, j]
            state[i][j] = 0
            break

sec = 0
while True:
    if not bfs(location):
        break
    if eat == size:
        eat = 0
        size += 1
print(sec)