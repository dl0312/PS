def solution(n, cores):
    start = 0
    end = 5000000000
    print(n, cores)
    n -= len(cores)
    if n < 0:
        for idx in range(len(cores)-1, -1, -1):
            n += 1
            if n == 0:
                return idx
    else:
        center = (start+end)//2
        while True:
            center = (start+end)//2
            task = 0
            for core in cores:
                task += center//core
            if task > n:
                if end > start + 1:
                    end = center
                else:
                    for idx in range(len(cores)-1, -1, -1):
                        if not center%cores[idx]:
                            task -= 1
                            if task == n:
                                return idx+1
            elif task < n:
                if end > start + 1:
                    start = center
                else:
                    for idx in range(len(cores)):
                        if not (center+1)%cores[idx]:
                            task += 1
                            if task == n:
                                return idx+1
            else:
                for idx in range(len(cores)-1, -1, -1):
                    if not center%cores[idx]:
                        return idx+1

n = 6
cores = [1,2,3]
print(solution(n, cores)) # 2

n = 1
cores = [1,2,3]
print(solution(n, cores)) # 1

n = 8
cores = [1,2,3]
print(solution(n, cores)) # 2
# for n in range(1, 500): # 처리해야 할 일의 수
#     for length in range(2, 100): # 코어의 수
#         cores = list(range(length+1,0, -1))
#         print(n, cores)
#         print(solution(n, cores))