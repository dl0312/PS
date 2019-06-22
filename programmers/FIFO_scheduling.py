import sys

def solution(n, cores):
    answer = 0
    min = sys.maxsize
    length = len(cores)
    if n <= length:
        return n

    for core in cores:
        if min > core:
            min = core

    start = (n//length)*min
    end = n*min
    center = (start+end)//2

    while start < end:
        print(start, end, center)
        cnt = 0
        available_cnt = 0
        for core in cores:
            cnt += (center//core)+1
            if center % core == 0:
                available_cnt += 1
                cnt -= 1
        if cnt >= n:
            end = center
        elif cnt + available_cnt < n:
            start = center + 1
        else:
            for i in range(length):
                if center % cores[i] == 0:
                    cnt += 1
                if cnt == n:
                    return i+1
        center = (start + end)//2

    return answer

n = 6
cores = [1,2,3]
print(solution(n, cores)) # 2

n = 1
cores = [1,2,3]
print(solution(n, cores)) # 1

n = 8
cores = [1,2,3]
print(solution(n, cores)) # 3

# 1, 2, 3 = 3
# 1, 1, 2 = 4
# 1, 2, 1 = 6
# 1, 1, 3 = 8

# for n in range(1, 500): # 처리해야 할 일의 수
#     for length in range(2, 100): # 코어의 수
#         cores = list(range(length+1,0, -1))
#         print(n, cores)
#         print(solution(n, cores))