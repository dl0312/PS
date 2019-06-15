def solution(n):
    tiles = [0]*5001
    tiles[0] = 1
    tiles[2] = 3
    for i in range(4, 5000, 2):
        tiles[i] = 3*tiles[i-2]%1000000007
        for j in range(i-4, -1, -2):
            if j >= 0:
                tiles[i] += tiles[j]*2
    tiles[0] = 0
    return tiles[n]%1000000007

N = 4
print(solution(N)) # 11
N = 2
print(solution(N)) # 3
N = 6
print(solution(N)) # 41
N = 8
print(solution(N)) # 153
# for i in range(2, 1000, 2):
#     print(solution(i))