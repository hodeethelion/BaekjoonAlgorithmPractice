import sys
test_case = int(sys.stdin.readline())
for _ in range(test_case):
    stud_score = list(map(int, sys.stdin.readline().split()))
    avg = sum(stud_score[1:])/ stud_score[0]
    over_std = 0
    for score in stud_score[1:]:
        if score > avg:
            over_std += 1
    print(f'{round(over_std*100/stud_score[0],3):.3f}%')