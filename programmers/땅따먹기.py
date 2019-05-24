def solution(land):
    raw_max = [0, 0, 0, 0]
    for raw in land:
        for idx in range(len(raw)):
            raw[idx] += max(raw_max[:idx] + raw_max[idx + 1:])
        raw_max = raw
    return max(raw_max)


land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
print(solution(land))  # 16
