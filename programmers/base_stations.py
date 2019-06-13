import math

def solution(n, stations, w):
    nonreachable_list = []
    current = 1
    range = 2*w+1
    for station in stations:
        if current >= station - w:
            current = station + w + 1
        else:
            nonreachable_list.append(station - w - current)
            current = station + w + 1
    if current < n+1:
        nonreachable_list.append(n - current + 1)
    answer = 0
    for nonreachable in nonreachable_list:
        answer += math.ceil(nonreachable/range)
    return answer

N = 11
stations = [4,11]
W = 1
print(solution(N, stations, W)) # 3
N = 16
stations = [9]
W = 2
print(solution(N, stations, W)) # 3
N = 5
stations = [3]
W = 1
print(solution(N, stations, W)) # 2
N = 5
stations = [2]
W = 1
print(solution(N, stations, W)) # 1
