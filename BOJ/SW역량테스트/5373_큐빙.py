def rotate(c):
    # 돌려야 하는 면을 기준으로 동서남북 면 배치
    if c == 'U':
        M, W, S, E, N = U, L, F, R, B
    if c == 'L':
        M, W, S, E, N = L, F, U, B, D
    if c == 'F':
        M, W, S, E, N = F, U, L, D, R
    if c == 'R':
        M, W, S, E, N = R, D, B, U, F
    if c == 'B':
        M, W, S, E, N = B, R, D, L, U
    if c == 'D':
        M, W, S, E, N = D, B, R, F, L
    
    # 가운데 면 회전
    M[0][2], M[1][2], M[2][2], M[2][1], M[2][0], M[1][0], M[0][0], M[0][1] = M[0][0], M[0][1], M[0][2], M[1][2], M[2][2], M[2][1], M[2][0], M[1][0]
    
    # 가운데 면이 회전됨에 따라 동서남북 면의 변화
    W[2][2], W[2][1], W[2][0], S[2][0], S[1][0], S[0][0], E[0][2], E[1][2], E[2][2], N[0][0], N[0][1], N[0][2] = S[2][0], S[1][0], S[0][0], E[0][2], E[1][2], E[2][2], N[0][0], N[0][1], N[0][2], W[2][2], W[2][1], W[2][0]


for _ in range(int(input())):
    U = [['w'] * 3 for _ in range(3)]   # 윗 면
    D = [['y'] * 3 for _ in range(3)]   # 아랫 면
    F = [['r'] * 3 for _ in range(3)]   # 앞 면
    B = [['o'] * 3 for _ in range(3)]   # 뒷 면
    L = [['g'] * 3 for _ in range(3)]   # 왼쪽 면
    R = [['b'] * 3 for _ in range(3)]   # 오른쪽 면
    n = int(input())
    turn = list(input().split())
    for a, d in turn:
        rotate(a)
        if d == '-':    # 반시계 방향인 경우 두번 더 돌리면 됨
            rotate(a)
            rotate(a)
    for i in range(3):
        print("".join(j for j in U[i]))