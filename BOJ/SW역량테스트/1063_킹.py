direction = {
    'R': [0, 1],
    'L': [0, -1],
    'B': [1, 0],
    'T': [-1, 0],
    'RT': [-1, 1],
    'LT': [-1, -1],
    'RB': [1, 1],
    'LB': [1, -1]
}

king, stone, N = input().split()
king_x, king_y = 8 - int(king[1]), ord(king[0]) - 65
stone_x, stone_y = 8 - int(stone[1]), ord(stone[0]) - 65

for _ in range(int(N)):
    d = input()
    if 0 <= king_x + direction[d][0] < 8 and 0 <= king_y + direction[d][1] < 8:
        king_x, king_y = king_x + direction[d][0], king_y + direction[d][1]
        if king_x == stone_x and king_y == stone_y:
            if 0 <= stone_x + direction[d][0] < 8 and 0 <= stone_y + direction[d][1] < 8:
                stone_x, stone_y = stone_x + direction[d][0], stone_y + direction[d][1]
            else:
                king_x, king_y = king_x - direction[d][0], king_y - direction[d][1]

print('{}{}'.format(chr(king_y + 65), 8 - king_x))
print('{}{}'.format(chr(stone_y + 65), 8 - stone_x))

