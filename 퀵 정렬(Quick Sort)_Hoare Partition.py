# Hoare-Partition 알고리즘
def quick_sort(arr, left, right):
    # pivot 위치 결정 (피복을 기준으로 큰 값은 오른쪽, 작은 값은 왼쪽으로 구분)
    # 왼쪽 부분집합 정렬
    # 오른쪽 부분집합 정렬
    if left < right:
        # 피봇 구하기
        pivot = hoare_partition(arr, left, right)
        # 왼쪽 부분집합 정렬 실행
        quick_sort(arr, left, pivot-1)
        # 오른쪽 부분집합 정렬 실행
        quick_sort(arr, pivot+1, right)

def hoare_partition(arr, left, right):
    # i, j 를 설정하고, 큰 값 찾고, 작은 값 찾아서 위치 바꿔주기
    i = left
    j = right
    pivot = arr[left]

    # i 가 j 보다 작을 때 까지 계속해서 반복
    while i <= j:
        # 피봇보다 큰 값이 나올 때 까지 i 증가
        while i <= j and arr[i] <= pivot:
            i += 1
        # 피봇보다 작은 값이 나올 때 까지 j 감소
        while i <= j and arr[j] >= pivot:
            j -= 1

        # i 가 j 보다 작으면, 위치 교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[left], arr[j] = arr[j], arr[left]

    return j

arr = [5, 4, 3, 6, 7, 9, 1, 2]
quick_sort(arr, 0, len(arr)-1)
print(arr)