# Hoare-Partition 알고리즘
def quick_sort(arr, left, right):
    # pivot 위치 결정 (피복을 기준으로 큰 값은 오른쪽, 작은 값은 왼쪽으로 구분)
    # 왼쪽 부분집합 정렬
    # 오른쪽 부분집합 정렬
    if left < right:
        # 피봇 구하기
        pivot = lomuto_partition(arr, left, right)
        # 왼쪽 부분집합 정렬 실행
        quick_sort(arr, left, pivot-1)
        # 오른쪽 부분집합 정렬 실행
        quick_sort(arr, pivot+1, right)

def lomuto_partition(arr, left, right):
    # 맨 오른쪽 요소를 pivot으로 설정하고,
    i = left - 1
    j = left
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        # arr[j] 가 pivot 보다 작으면, i 를 1 증가
        if arr[j] < pivot:
            i += 1
        # arr[j], arr[i] 위치 교환
            arr[i], arr[j] = arr[j], arr[i]

    # i 가 가리키는 위치가 pivot 보다 작은 값의 마지막 인덱스
    # i + 1 의 위치에 pivot 을 두고 i + 1 반환
    arr[i + 1] , arr[right] = arr[right], arr[i + 1]
    return i + 1