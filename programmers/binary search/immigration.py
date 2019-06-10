import sys

def solution(n, times):
    times.sort()
    start = 0
    end = 1000000000 * 1000000000 * 2
    while True:
        people = 0
        center = (start+end)//2
        if end == start + 1:
            start_people = 0
            end_people = 0
            for time in times:
                start_people += center // time
            for time in times:
                end_people += center // time
            if start_people == n:
                return start
            elif start_people < n:
                return end
        for time in times:
            people += center//time
        print(start, end, people)
        if people > n:
            end = center
        elif people < n:
            start = center
        else:
            break
    center = (start+end)//2
    min_mod = sys.maxsize
    for time in times:
        div, mod = divmod(center, time)
        if not mod:
            break;
        else:
            if min_mod > mod:
                min_mod = mod
    else:
        return center - min_mod
    return center


n = 6
times = [7, 10]
print(solution(n, times)) # 28
n = 1
times = [1, 1]
print(solution(n, times)) # 1
n = 6
times = [7, 10]
print(solution(n, times)) # 28