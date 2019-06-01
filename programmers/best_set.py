def solution(n, s):
    result = 0
    if s > n-1:
        div, mod = divmod(s, n)
        result = [div] * n
        for i in range(mod):
            result[-1*(i+1)] += 1
    else:
        return [-1]
    return result

n = 2
s = 9
print(solution(n, s)) # [4, 5]
n = 3
s = 9
print(solution(n, s)) # [3, 3, 3] or [2, 3, 4]
n = 3
s = 10
print(solution(n, s)) # [3, 3, 4] or [2, 3, 5]
n = 3
s = 11
print(solution(n, s)) # [3, 4, 4] or [2, 4, 5]
n = 2
s = 1
print(solution(n, s)) # [-1]