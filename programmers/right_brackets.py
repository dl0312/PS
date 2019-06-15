def solution(n):
    curr_list = [0]*(n+1)
    curr_list[1] = 1
    for i in range(1,2*n):
        next_list = [0]*(n+1)
        for i in range(n+1):
            if i == 0:
                next_list[i+1] += curr_list[i]
            elif i == n:
                next_list[i-1] += curr_list[i]
            else:
                next_list[i+1] += curr_list[i]
                next_list[i-1] += curr_list[i]
        curr_list = next_list
    return curr_list[0]

N = 2
print(solution(N)) # 2
N = 3
print(solution(N)) # 5
