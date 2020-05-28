def backtrack(selected, idx, input):
    # selected : 각 노드의 선택 여부를 판단하는 배열
    # idx : 깊이
    # input : 목표 개수
    candidates = [0] * 2    # 선택할 수 있는 선택지는 O/X
    if idx == input:
        for i in range(input):
            if selected[i]:
                print(i, end = " ")
        print()
        return
    else:
        n_candidate = make_candidate(candidates)    # 후보군 생성
        for i in range(n_candidate):
            selected[idx] = candidates[i]
            backtrack(selected, idx + 1, input)


def make_candidate(candidates):
    candidates[0] = 1
    candidates[1] = 0
    return 2


N = 5
backtrack([0] * N, 0, N)