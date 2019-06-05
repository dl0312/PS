def calculate_budget(candidate, budgets):
    temp = 0
    for budget in budgets:
        if candidate > budget:
            temp += budget
        else:
            temp += candidate
    return temp

def solution(budgets, M):
    budgets.sort()
    length = len(budgets)
    start = budgets[0]
    end = budgets[-1]
    average = M//length
    if start >= average:
        return average
    elif end <= average:
        return end
    else:
        while True:
            candidate = (start + end)//2
            temp = calculate_budget(candidate, budgets)
            if temp > M:
                end = candidate
            elif temp < M:
                if candidate == start:
                    if calculate_budget(end,budgets) < M:
                        return end
                    else: return start
                start = candidate
            elif temp == M:
                return candidate

budgets = [120, 110, 140, 150]
M = 485
print(solution(budgets, M)) # 127
budgets = [120, 110, 140, 150]
M = 488
print(solution(budgets, M)) # 128