def hanoi(n, a, b, c):
    answer = []
    if n == 1:
        answer.append([a,c])
    else:
        for way in hanoi(n-1, a, c, b):
            answer.append(way)
        answer.append([a,c])
        for way in hanoi(n-1, b, a, c):
            answer.append(way)
    return answer

def solution(n):
    return hanoi(n, 1, 2, 3)

n = 2
print(solution(n)) # [[1, 2], [1, 3], [2, 3]]
n = 3
print(solution(n)) # [[1, 3], [1, 2], [3, 2], [1, 3], [2, 1], [2, 3], [1, 3]]
n = 4
print(solution(n)) # [[1, 2], [1, 3], [2, 3], [1, 2],