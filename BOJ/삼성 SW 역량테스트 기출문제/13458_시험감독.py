N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0
for x in A:
    result += 1
    if x <= B:
        continue
    else:
        if (x - B) % C:
            result += (x - B) // C + 1
        else:
            result += (x - B) // C
print(result)

# import math

# N = int(input())
# A = list(map(int, input().split()))
# B, C = map(int, input().split())
# result = 0
# for x in A:
#     result += 1
#     if x <= B:
#         continue
#     else:
#         result += math.ceil((x - B) / C)
# print(result)