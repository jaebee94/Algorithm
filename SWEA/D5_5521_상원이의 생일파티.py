def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    bfs(1)
    cnt = 0
    for visit in visited:
        if visit in [2, 3]:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
