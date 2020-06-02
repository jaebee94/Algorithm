def hanoi(block, a, b, c, process):
    if block == 1:
        return process.append([a, c])
    else:
        hanoi(block - 1, a, c, b, process)
        process.append([a, c])
        hanoi(block - 1, b, a, c, process)

def solution(n):
    process = []
    hanoi(n, 1, 2, 3, process)
    return process

print(solution(2))