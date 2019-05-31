def solution(m, n, puddles):
    answer = 0
    road = [[0 for i in range(m+1)] for j in range(n+1)]
    road[1][1] = 1
    for row in road:
        print(row)
    print()
    for i in range(3, m+n+1):
        for j in range(1, i):
            x = i-j
            y = j
            if x <= m and y <= n:
                if [x, y] not in puddles:
                    cnt = 0
                    if y-1 > 0:
                        if [x, y-1] not in puddles:
                            cnt += road[y-1][x]
                    if x-1 > 0:
                        if [x-1, y] not in puddles:
                            cnt += road[y][x-1]
                    road[y][x] = cnt % 1000000007
    for row in road:
        print(row)
    return road[n][m]


m = 4
n = 3
puddles = [[2,2], [1,3]]
print(solution(m,n,puddles)) # 4
m = 10
n = 10
puddles = []
print(solution(m,n,puddles)) # 4
m = 100
n = 100
puddles = []
print(solution(m,n,puddles)) # 4