def solution(n, a, b):
    if a > b:
        a, b = b, a
    round = 1
    while True:
        if b - a == 1 and a % 2 == 1:
            if a == n / (2 ** round):
                if a == 1:
                    break
            else:
                break
        a = (a + 1) // 2
        b = (b + 1) // 2
        round += 1
    return round


n = 8
a = 7
b = 4
print(solution(n, a, b))  # 3
n = 8
a = 4
b = 7
print(solution(n, a, b))  # 3
n = 2
a = 2
b = 1
print(solution(n, a, b))  # 1
n = 4
a = 1
b = 2
print(solution(n, a, b))  # 1
n = 8
for i in range(1, n):
    for j in range(i + 1, n + 1):
        print(i, j, solution(n, j, i))
n = 4
a = 1
b = 4
print(solution(n, a, b))  # 2
n = 16
a = 8
b = 9
print(solution(n, a, b))  # 4
