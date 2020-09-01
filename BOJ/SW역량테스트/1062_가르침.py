from itertools import combinations

N, K = map(int, input().split())
basic_set = {'a', 'c', 'i', 'n', 't'}
words = [set(input()) - basic_set for _ in range(N)]
chars = set()
for word in words:
    chars = chars | word

max_len = len(chars - basic_set)

if K - 5 < 0:
    print(0)
elif K - 5 >= max_len:
    print(N)
else:
    max_cnt = 0
    for candidate in combinations(chars, K - 5):
        cnt = 0
        for word in words:
            if not set(candidate) - word:
                cnt += 1
        max_cnt = max(max_cnt, cnt)
    print(max_cnt)

