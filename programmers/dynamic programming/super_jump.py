def solution(n):
    case_lst = [0]*(n+1)
    case_lst[0] = 1
    for i in range(1, n+1):
        if i == 1:
            case_lst[i] = case_lst[i-1]
        else:
            case_lst[i] = case_lst[i-1] + case_lst[i-2]
    return case_lst[-1]%1234567
n = 1
print(solution(n)) # 1
n = 4
print(solution(n)) # 5
n = 3
print(solution(n)) # 3