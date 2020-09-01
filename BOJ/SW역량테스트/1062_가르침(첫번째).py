from itertools import combinations

N, K = map(int, input().split())
basic_set = {'a', 'c', 'i', 'n', 't'}
words = [set(input()) - basic_set for _ in range(N)]
chars = set()
for word in words:
    chars = chars | word

max_len = len(chars)

if K - 5 < 0:
    print(0)
elif K - 5 >= max_len:
    print(N)
else:
    candidates = list(combinations(chars, K - 5))
    max_cnt = 0
    for candidate in candidates:
        cnt = 0
        for word in words:
            for char in word:
                if char not in candidate:
                    break
            else:
                cnt += 1
        max_cnt = max(max_cnt, cnt)
    print(max_cnt)