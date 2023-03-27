import sys
input = sys.stdin.readline
n_test = int(input())
for _ in range(n_test):
    n_people = int(input())
    # print(n_people)
    grade_list = [] 
    for _ in range(n_people):
        a, b = map(int, input().split())
        grade_list.append([a,b])
    grade_list.sort(key=lambda x: x[0])
    # print(grade_list)
    min_2nd_grade  = grade_list[0][1]
    cnt = 1 
    for i in range(1, n_people):
        if grade_list[i][1] > min_2nd_grade:
            continue
        else:
            cnt += 1
            min_2nd_grade = grade_list[i][1]
    print(cnt)
