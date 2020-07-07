from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
players = [i for i in range(N)]
team = list(combinations(players, N//2))
start = []
link = []
answer = 200*N

for _ in range(len(team)//2):
    start.append(team.pop(0))
    link.append(team.pop())
print(start, link)
for i in range(len(start)):
    ability_start, ability_link = 0, 0
    for x in range(0, len(start[i])-1):
        for y in range(x+1, len(start[i])):
            ability_start += S[start[i][x]][start[i][y]] + S[start[i][y]][start[i][x]]
            ability_link += S[link[i][x]][link[i][y]] + S[link[i][y]][link[i][x]]
    answer = min(answer, abs(ability_start - ability_link))

print(answer)