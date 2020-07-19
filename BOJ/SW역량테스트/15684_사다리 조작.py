n, m, h = map(int, input().split())
board = [[0] * n for _ in range(h)]
ans = 4

for _ in range(m):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

def ladder():
    for i in range(n):
        tmp = i
        for j in range(h):
            if board[j][tmp]:
                tmp += 1
            elif tmp > 0 and board[j][tmp-1]:
                tmp -= 1
        if i != tmp:
            return False
    return True

def solve(cnt, a, b):
    global ans

    if ans <= cnt:
        return
    if ladder():
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return
    for i in range(a, h):
        if i == a:
            k = b
        else:
            k = 0
        
        for j in range(k, n-1):
            if board[i][j]:
                j += 1
            else:
                board[i][j] = 1
                solve(cnt+1, i, j+2)
                board[i][j] = 0

solve(0, 0, 0)
if ans < 4:
    print(ans)
else:
    print(-1)