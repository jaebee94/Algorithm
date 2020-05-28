# 반복 구조
def binarySearch(n, S, key):
    low = 0
    high = n - 1

    while low <= high and location = 0:
        mid = low + (high - low) / 2
        if S[mid] == key:
            return mid
        elif S[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# 재귀 구조
def binarySearch(S, low, high, key):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if key == S[mid]:
            return mid
        elif key < S[mid]:
            return binarySearch(S, low, mid - 1, key)
        else:
            return binarySearch(S, mid + 1, high, key)