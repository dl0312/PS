def solution(n):
    answer = 0
    while n != 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            answer += 1
    return answer

n = 5
print(solution(n)) # 2
n = 6
print(solution(n)) # 2
n = 5000
print(solution(n)) # 5
n = 1000000000
print(solution(n)) # 5