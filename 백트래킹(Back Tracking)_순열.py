def backtrack(result, selected, idx, N):
    if idx == N:
        print(result)
        return

    # 사용가능한 선택지 후보군에 대하여 다음 단계로 진행
    for i in range(N):
        if not selected[i]:
            selected[i] = 1
            result[idx] = i
            backtrack(result, selected, idx+1, N)
            selected[i] = 0

N = 5
backtrack([0] * N, [0] * N, 0, N)


# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 에서 원소의 합이 10인 부분집합 모두 출력하기
# def backtrack(arr, idx, N, selected, sum_num):
#     if sum_num > 10:
#         return
#     if idx == N:
#         # 총합이 10 인 경우에만 출력
#         if sum_num == 10:
#             for i in range(N):
#                 if selected[i]:
#                     print(arr[i], end=" ")
#             print()
#         return
#     selected[idx] = 1
#     sum_num += arr[idx]
#     backtrack(arr, idx+1, N, selected, sum_num) # 앞 뒤로 sum_num 을 더하고 빼는 과정을 없애려면 sum_num + arr[idx] 를 인자로 넘기면 된다.

#     selected[idx] = 0
#     sum_num -= arr[idx]
#     backtrack(arr, idx+1, N, selected, sum_num) # 여기는 sum_num 넘긴다.

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# backtrack(arr, 0, 10, [0]*10, 0)