def solution(n, k):
    # 각 자리수 마다 순열의 개수 구하기
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] * i)
    
    init = 0    # n 번째 순열의 첫번째에 오는 숫자
    perm = []   # 만들어지는 순열
    length = n  # 처음의 n 저장
    while True:
        # 1 부터 n 까지 사용하지 않은 숫자 저장
        arr = [i for i in range(1, length+1) if i not in perm]
        
        # n == 1일때는 예외처리 -> 결과 도출
        if n == 1:
            perm.append(arr[0])
            return perm
        
        # k 번째 오는 순열의 첫번째 숫자의 인덱스 구하기
        init = (k-1) // dp[n-1]
        perm.append(arr[init])
        
        k = k % dp[n-1]
        n -= 1