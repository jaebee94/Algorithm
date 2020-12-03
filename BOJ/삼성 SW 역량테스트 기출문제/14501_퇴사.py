N = int(input())
plan = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)
for i in range(N-1, -1, -1):
    if i + plan[i][0] <= N:
        dp[i] = max(dp[i+plan[i][0]] + plan[i][1], dp[i+1])
    else:
        dp[i] = dp[i+1]
print(dp[0])