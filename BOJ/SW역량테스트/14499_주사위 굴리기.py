N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
play = list(map(int, input().split()))
dice = [0] * 6
i, j = x, y
for turn in play:
    if turn == 1:
        j = y + 1
        next_dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif turn == 2:
        j = y - 1
        next_dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif turn == 3:
        i = x - 1
        next_dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    else:
        i = x + 1
        next_dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]

    if 0 <= i and i < N and 0 <= j and j < M:
        if board[i][j] != 0:
            next_dice[0] = board[i][j]
            board[i][j] = 0
        else:
            board[i][j] = next_dice[0]

        dice = next_dice.copy()
        x, y = i, j
        print(dice[5])
    else:
        i, j = x, y
