def solution(m, n, board):
    answer = 0
    check = [[0]*n for _ in range(m)]
    for i in range(m):
        board[i] = list(board[i])
    
    while True:
        # 지울 수 있는 블록 탐색
        flag = True
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != 0:
                    check[i][j] = check[i][j+1] = check[i+1][j] = check[i+1][j+1] = 1
                    flag = False
        # 지울 수 있는 블록이 없으면 while 문 종료
        if flag:
            break
        
        # 지울 수 있는 블록 지우기
        for x in range(m):
            for y in range(n):
                if check[x][y] == 1:
                    board[x][y] = 0
                    check[x][y] = 0
        
        # 밑에서 부터 비어있는 블록이면 옮기기
        for j in range(n):
            for i in range(m-1, -1, -1):
                if board[i][j] == 0:
                    target = (i, j)
                    for x in range(target[0]-1, -1, -1):
                        if board[x][j] != 0:
                            board[target[0]][target[1]] = board[x][j]
                            board[x][j] = 0
                            target = (target[0]-1, target[1])
                    break

    for i in board:
        for j in i:
            if j == 0:
                answer += 1
        
    return answer