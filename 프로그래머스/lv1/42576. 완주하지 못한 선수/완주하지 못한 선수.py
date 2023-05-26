from collections import defaultdict

def solution(participant, completion):
    complete_people = defaultdict(int)
    answer=''
    for person in completion:
        complete_people[person] += 1
    for pers in participant:
        complete_people[pers] -= 1
    reverse_dict = dict(map(reversed, complete_people.items()))
    print(reverse_dict[-1])
    
    return reverse_dict[-1]