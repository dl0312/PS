def solution(people, limit):
    people.sort()
    boat = 0
    length = len(people)
    l_idx = 0
    r_idx = length - 1
    while l_idx < r_idx:
        if people[l_idx] + people[r_idx] <= limit:
            boat += 1
            r_idx -= 1
            l_idx += 1
        else:
            r_idx -= 1
            boat += 1
    if r_idx == l_idx:
        boat += 1
    return boat


people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))  # 3
people = [70, 80, 50]
limit = 100
print(solution(people, limit))  # 3
people = [10, 20, 30, 40, 50, 60, 70, 80, 90]
limit = 100
print(solution(people, limit))  # 5
people = [10, 20, 30, 40, 50, 50, 60, 70, 80, 90]
limit = 100
print(solution(people, limit))  # 5
people = [10, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99, 99]
limit = 100
print(solution(people, limit))  # 8
people = [50, 50, 50, 50]
limit = 100
print(solution(people, limit))  # 2
people = [50]
limit = 100
print(solution(people, limit))  # 1
people = [100, 1]
limit = 100
print(solution(people, limit))  # 2
