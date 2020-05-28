# ex) N-Queen
def backtrack(idx): # idx = 행
    global N, cnt
    # 최종 상태인지 확인하고, 최종 상태이면 해 이다.
    if idx == N:
        # 다 찾았음 -> 해
        cnt += 1
        return
    # 해당 상태에서 선택할 수 있는 후보군 생성
    # 노드가 유망한지 확인 : 열, 상향 대각, 하향 대각
    for i in range(N):
        if not col[i] and not dia_1[idx + i] and not dia_2[N + i - idx - 1]:
            # 모든 후보군에 대해서 다음 상태 실행
            col[i] = 1
            dia_1[idx+i] = 1
            dia_2[N + i - idx - 1] = 1
            # 재귀 실행
            backtrack(idx + 1)
            # 초기화
            col[i] = 0
            dia_1[idx+i] = 0
            dia_2[N + i - idx - 1] = 0
            

N = 4
col = [0] * N   # 열의 사용여부를 판단하는 리스트
# 대각 유망성을 판단할 리스트
# 상향 대각은 i, j 의 합이 같음
# 하향 대각은 i, j 의 차가 같음
dia_1 = [0] * (2 * N - 1)   # i + j
dia_2 = [0] * (2 * N - 1)   # N + j - i - 1
cnt = 0
backtrack(0)
print(cnt)
# 각 행에는 1개의 퀸만 올 수 있다.