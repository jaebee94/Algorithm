from collections import deque

N, K = map(int, input().split())
q = deque()
visit = [0 for _ in range(100001)]
q.append((N, 0))
while True:
    (x, t) = q.popleft()
    if x == K:
        print(t)
        break
    if not visit[x]:
        visit[x] = 1
        if x-1 >= 0:
            q.append((x-1, t+1))
        if 2*x <= 100000:
            q.append((2*x, t+1))
        if x+1 <= 100000:
            q.append((x+1, t+1))