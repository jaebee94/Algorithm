import itertools

n,m = map(int, input().split())

homes = []
chickens = []

# 도시 정보
city = [list(map(int, input().split())) for _ in range(n)]
 
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            homes.append([i,j])
        if city[i][j] == 2:
            chickens.append([i,j])

# 도시에 있을 수 있는 최대의 치킨집 수 에 따라 치킨집들로 조합
chicken_list = list(itertools.combinations(chickens, m))

answer = 1000000
# 치킨집 들의 모든 조합에 대해
for chickens in chicken_list:
    # 집과 치킨집들의 치킨거리를 계산
    total = 0
    for home in homes:
        minn = 10000000
        # 선택된 집과 조합 리스트 안의 m개의 치킨집 거리 중 짧은 거리를 선택
        for chicken in chickens:
            minn = min(minn, abs(chicken[0] - home[0]) + abs(chicken[1] - home[1]))
        # 도시의 치킨거리에 더함
        total += minn
    answer = min(answer, total)
print(answer)