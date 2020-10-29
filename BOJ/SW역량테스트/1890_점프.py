N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            break

        b = i + board[i][j]
        r = j + board[i][j]
        
        if b < N:
            dp[b][j] += dp[i][j]
        if r < N:
            dp[i][r] += dp[i][j]

print(dp[N-1][N-1])
