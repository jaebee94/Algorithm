N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort()
answer = 0
for i in range(N):
    answer += a[i] * b[i]
print(answer)