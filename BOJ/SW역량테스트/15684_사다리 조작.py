n, m, h = map(int, input().split())
board = [[0] * n for _ in range(h)]
ans = 4

for _ in range(m):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

# 제대로 연결된 사다리인지 확인
def ladder():
    for i in range(n):
        tmp = i
        for j in range(h):
            # 사다리 따라 움직이는 절차
            if board[j][tmp]:
                tmp += 1
            elif tmp > 0 and board[j][tmp-1]:
                tmp -= 1
        if i != tmp:
            return False
    # i == tmp 여야 정상적인 사다리라고 판단 -> True 리턴
    return True

def solve(cnt, a, b):
    global ans
    # 계속해서 넘어오는 cnt 가 현재까지 도출한 ans 보다 크면 리턴
    if ans <= cnt:
        return
    # 완벽한 사다리가 되었으면 더 이상 가로줄을 놓지 않아도 되니까 리턴
    if ladder():
        ans = min(ans, cnt)
        return
    # 최대 3 까지니까 리턴
    if cnt == 3:
        return

    for i in range(a, h):
        if i == a:
            k = b
        else:
            k = 0
        
        for j in range(k, n-1):
            # 사다리가 연결되어 있으면 연속해서 가로줄을 만들면 안되니까 j += 1
            if board[i][j]:
                j += 1
            # 사다리가 연결되어 있지 않으면 가로줄을 만들어주고 j += 1 하여 재귀 호출
            else:
                board[i][j] = 1
                solve(cnt+1, i, j+2)
                board[i][j] = 0

solve(0, 0, 0)
if ans < 4:
    print(ans)
else:
    print(-1)