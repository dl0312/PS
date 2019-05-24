def solution(numbers):
    numbers = sorted(numbers, key=lambda n: n / int('1' * (len(str(n)))), reverse=True)
    answer= ""
    for n in numbers:
        answer += str(n)
    return str(int(answer))

numbers = [6, 10, 2]
print(solution(numbers))
numbers = [3, 30, 34, 5, 9]
print(solution(numbers))
numbers = [3, 30, 31, 34, 50, 5, 51, 9, 0]
print(solution(numbers))
numbers = [0, 10, 999]
print(solution(numbers))