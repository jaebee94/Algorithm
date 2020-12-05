from collections import deque

def spring():
    i = 0
    while i < len(trees):
        if nutrients[trees[i][0] - 1][trees[i][1] - 1] >= trees[i][2]:
            nutrients[trees[i][0] - 1][trees[i][1] - 1] -= trees[i][2]
            trees[i][2] += 1
            i += 1
        else:
            break
            # dead.append(trees.pop(i))

def summer():
    for tree in dead:
        nutrients[tree[0] - 1][tree[1] - 1] += tree[2] // 2
        tree[2] = 0
    return


def autumn():
    for tree in trees:
        if tree[2] % 5 == 0 and tree[2] != 0:
            for k in range(8):
                ni = tree[0] + di[k]
                nj = tree[1] + dj[k]
                if 0 < ni < N + 1 and 0 < nj < N + 1:
                    trees.append([ni, nj, 1])
    return


def winter():
    for i in range(N):
        for j in range(N):
            nutrients[i][j] += A[i][j]
    return


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
trees = [list(map(int, input().split())) for _ in range(M)]
nutrients = [[5] * N for _ in range(N)]
q = [[deque() for _ in range(N)] for _ in range(N)]
for tree in trees:
    q[tree[0]-1][tree[1]-1].append(tree[2])
dead = []

di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

for _ in range(K):
    spring()
    summer()
    autumn()
    winter()

answer = len(trees)
for tree in trees:
    if tree[2] == 0:
        answer -= 1
print(answer)
