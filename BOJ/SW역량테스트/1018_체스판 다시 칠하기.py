def paint(copy_board, i, j):
    change = 0
    for x in range(i, i+8):
        if x != i:
            if copy_board[x-1][j] == copy_board[x][j]:
                change += 1
                if copy_board[x][j] == 'W':
                    copy_board[x][j] = 'B'
                else:
                    copy_board[x][j] = 'W'
        for y in range(j+1, j+8):
            if change >= minV:
                return 64
            if copy_board[x][y-1] == copy_board[x][y]:
                change += 1
                if copy_board[x][y] == 'W':
                    copy_board[x][y] = 'B'
                else:
                    copy_board[x][y] = 'W'
    return change


import copy

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
minV = 64
for i in range(N - 7):
    for j in range(M - 7):
        if board[i][j] == 'W':
            copy_board = copy.deepcopy(board)
            minV = min(minV, paint(copy_board, i, j))
            copy_board = copy.deepcopy(board)
            copy_board[i][j] = 'B'
            minV = min(minV, paint(copy_board, i, j)+1)
        else:
            copy_board = copy.deepcopy(board)
            minV = min(minV, paint(copy_board, i, j))
            copy_board = copy.deepcopy(board)
            copy_board[i][j] = 'W'
            minV = min(minV, paint(copy_board, i, j)+1)
print(minV)
