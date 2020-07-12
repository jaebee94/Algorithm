import copy

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# cctv의 종류 별 탐색 방향
di = [0, [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [0, 3]], [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]], [[0, 1, 2, 3]]]

minv = n * m
def dfs(start, office, s):
    global minv

    # cctv를 모두 탐색하면 사각지대를 count하고 재귀 종료
    if start == len(s):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if office[i][j] == 0:
                    cnt += 1
        minv = min(minv, cnt)
        return
    
    num, x, y = s[start]
    # 해당 cctv가 탐색할 수 있는 방향
    for direction in di[num]:
        tmp = copy.deepcopy(office)
        # 각 방향의 구역 탐색 완료 표시
        for i in direction:
            nx, ny = x + dx[i], y + dy[i]
            while n > nx >= 0 and m > ny >= 0:
                # 벽 만나면 종료
                if tmp[nx][ny] == 6:
                    break
                elif tmp[nx][ny] == 0:
                    tmp[nx][ny] = '#'
                nx += dx[i]
                ny += dy[i]
        # 다음 cctv 확인
        dfs(start+1, tmp, s)

s = []
for i in range(n):
    for j in range(m):
        if office[i][j] not in [0, 6]:
            s.append([office[i][j], i, j])

dfs(0, office, s)
print(minv)
            