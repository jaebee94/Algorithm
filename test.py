def solution(maps):
    answer = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    n = len(maps)
    m = len(maps[0])
    visit = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and not visit[i][j]:
                cnt = 0
                sub = 0
                s = [(i, j)]
                while s:
                    start_i, start_j = s.pop()
                    visit[start_i][start_j] = True
                    cnt += 1
                    for k in range(4):
                        ni = start_i + di[k]
                        nj = start_j + dj[k]
                        if 0 <= ni < n and 0 <= nj < m:
                            if maps[ni][nj] == 1 and not visit[ni][nj]:
                                s.append((ni, nj))
                            elif visit[ni][nj]:
                                sub += 1
                answer += cnt * 4 - sub * 2
    return answer

arr1 = [[0, 0, 1, 0, 0], [0, 1, 1, 0, 1], [0, 0, 1, 0, 1], [1, 1, 1, 0, 1]]
arr2 = [[1, 0, 1, 1], [0, 0, 1, 1], [1, 1, 0, 1], [1, 1, 0, 0]]
print(solution(arr1))
print(solution(arr2))