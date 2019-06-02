def solution(n, works):
    works.sort(reverse=True)
    sum_works = sum(works)
    len_works = len(works)
    answer = 0;
    if sum_works < n:
        return 0
    else:
        acc = 0
        idx = 0
        for i in range(len_works-1):
            if acc + (i+1)*(works[i] - works[i+1]) > n:
                idx = i+1
                break
            acc += (i + 1) * (works[i] - works[i + 1])
            for j in range(i+1):
                works[j] = works[i+1]
        else:
            for i in range(n - acc):
                works[i%(len_works)] -= 1
            for work in works:
                answer += work ** 2
            return answer
        for j in range(n - acc):
            works[j%(idx)] -= 1
        for work in works:
            answer += work ** 2
        return answer

works = [4, 3, 3]
n = 4
print(solution(n, works)) # 12
works = [2, 1, 2]
n = 1
print(solution(n, works)) # 6
works = [1, 1]
n = 3
print(solution(n, works)) # 0
works = [10, 1]
n = 3
print(solution(n, works)) # 50
works = [1, 1]
n = 3
print(solution(n, works)) # 0
