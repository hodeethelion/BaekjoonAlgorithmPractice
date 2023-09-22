# import sys
# input = sys.stdin.readline
from itertools import combinations
n_player = int(input())
total_table = []
new_table = [[0 for _ in range(n_player)] for _ in range(n_player)]

for i in range(n_player):
    total_table.append(list(map(int, input().split())))

for row in range(n_player):
    for col in range(n_player):
        new_table[row][col] = total_table[row][col] + total_table[col][row]
# 팀 짜기
team_list = list(combinations(range(n_player), n_player//2))

ans = 10000000000000000000
for team_a in team_list:
    candidate = 0
    team_b = list(range(n_player))
    for item in team_a:
        team_b.remove(item)
    combo_a = combinations(team_a, 2)
    combo_b = combinations(team_b, 2)
    # team_a 합, team_b 차
    for item in combo_a:
        candidate += new_table[item[0]][item[1]]
    for item2 in combo_b:
        candidate -= new_table[item2[0]][item2[1]]

    # print('candidate', candidate)
    if ans > abs(candidate):
        ans = abs(candidate)

print(ans)
