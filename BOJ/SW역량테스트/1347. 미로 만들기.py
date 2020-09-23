l = int(input())
move = list(input())

di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]
maze = [[False] * 101 for _ in range(101)]
i, j = 50, 50
k = 0
min_i, min_j, max_i, max_j = i, j, i, j
maze[i][j] = True
for x in move:
    if x == 'R':
        k = (k + 1) % 4
    elif x == 'L':
        k = (k + 3) % 4
    else:
        i, j = i + di[k], j + dj[k]
        maze[i][j] = True

    min_i = min(min_i, i)
    min_j = min(min_j, j)
    max_i = max(max_i, i)
    max_j = max(max_j, j)

for i in range(min_i, max_i+1):
    for j in range(min_j, max_j+1):
        if maze[i][j]:
            print('.', end='')
        else:
            print('#', end='')
    print()