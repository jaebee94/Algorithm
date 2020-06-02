def solution(n, s):
#     # sol. 1
#     from itertools import product
    
#     perms = list(product([1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=n))
#     s_perms = []
#     for perm in perms:
#         if sum(perm) == s:
#             s_perms.append(list(perm))
    
#     answer = []
#     max_result = 0
#     for perm in s_perms:
#         result = 1
#         for num in perm:
#             result *= num
#         if max_result < result:
#             max_result = result
#             answer = perm
#     if answer:
#         return answer
#     else:
#         return [-1]

    # sol. 2
    if s // n == 0:
        return [-1]
    else:
        return [s // n] * (n - s % n) + [s // n + 1] * (s % n)