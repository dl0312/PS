def solution(n, results):
    answer = 0
    people = {}
    for i in range(1, n+1):
        people[i] = [set(), set()] # win, lose
    results.sort()
    for result in results:
        winner, loser = result
        people[loser][0].add(winner)
        people[winner][1].add(loser)
    for i in range(1, n+1):
        if len(people[i][0] | people[i][1]) != n-1:
            stack = people[i][0].copy()
            while stack:
                item = stack.pop()
                people[i][0] = people[i][0] | people[item][0]
                if item > i:
                    stack |= people[item][0]
            stack = people[i][1].copy()
            while stack:
                item = stack.pop()
                people[i][1] = people[i][1] | people[item][1]
                if item > i:
                    stack |= people[item][1]
        if len(people[i][0] | people[i][1]) == n-1:
            answer += 1
    return answer

n= 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results)) # 2
n= 2
results = [[1, 2]]
print(solution(n, results)) # 2
n= 4
results = [[1, 2], [2, 3], [3, 4]]
print(solution(n, results)) # 4
n= 6
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [2, 6]]
print(solution(n, results)) # 1
n= 5
results = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 5]]
print(solution(n, results)) # 1

n= 5
results = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 3]]
print(solution(n, results)) # 5