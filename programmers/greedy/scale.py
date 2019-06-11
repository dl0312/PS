def solution(weight):
    weight.sort()
    sum_chu = 0
    for chu in weight:
        if chu > sum_chu +1:
            return sum_chu + 1
        else:
            sum_chu += chu
    return sum_chu + 1

weight = [3, 1, 6, 2, 7, 30, 1]
print(solution(weight)) # 21
weight = [1, 1, 3, 6, 10]
print(solution(weight)) # 2