def SelectionSort(A):
    n = len(A)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n): # for 문 계속 돌면서 제일 작은 값 탐색
            if A[j] < A[min]:
                min = j # 갱신
        A[min], A[i] = A[i], A[min] # 최소값 unsorted 인 영억의 제일 첫 인덱스로



        # [ 4, 2, 5, 1 ]
        # => step <=
        # min = 0 (A[min] = 4) -> 2, 5, 1 을 탐색하면서 제일 작은 값 탐색 -> 제일 앞으로
        # -> 1 2 5 4
        # min = 1 (A[min] = 2) -> 5, 4 탐색
        # -> 1 2 5 4
        # min = 2 (5) -> 4 탐색
        # -> 1 2 4 5
