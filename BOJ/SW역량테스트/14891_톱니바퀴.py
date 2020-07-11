states = [list(input()) for _ in range(4)]
K = int(input())
nd = [list(map(int, input().split())) for _ in range(K)]

# 회전 시켜야 하는 톱니 체크리스트 초기화
check = [False] * 4
score = 0
for (n, d) in nd:
    check[n-1] = True

    # n번의 톱니 양쪽으로 회전 시켜야 하는지 체크
    for i in range(n-1, 3):
        if states[i][2] != states[i+1][6]:
            check[i+1] = True
        else:
            break
    for j in range(n-1, 0, -1):
        if states[j][6] != states[j-1][2]:
            check[j-1] = True
        else:
            break
    
    # n이 짝수인 경우
    if n % 2 == 0:
        d *= -1

    # 체크리스트를 참조해서 회전
    for x in range(4):
        if check[x] == True:
            if d == 1:
                states[x][0], states[x][1:8] = states[x][-1], states[x][:7]
            else:
                states[x][:7], states[x][-1] = states[x][1:8], states[x][0]
        d *= -1
    check = [False] * 4

# 점수 합산
for i in range(4):
    if states[i][0] == '1':
        score += 2**i

print(score)            
