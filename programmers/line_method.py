def solution(n, k):
    k -= 1
    factorials = [1]
    base = [i+1 for i in range(n)]
    for i in range(2, 21):
        factorials.append(factorials[i-2]*i)
    result = []
    for i in range(n-1, -1, -1):
        div, mod = divmod(k, factorials[i-1])
        result.append(base[div])
        base.pop(div)
        k = mod
    return result


n = 3
k = 5
print(solution(n, k))  # [3, 1, 2]
n = 20
k = 20*19*18*17
print(solution(n, k))  # [3, 1, 2]
