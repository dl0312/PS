def solution(N, stages):
    result = {} # 스테이지별 실패율
    denominator = len(stages) # 스테이지를 클리어한 플레이어
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)

N = 5
stages = [2,1,2,6,2,4,3,3]
print(solution(N,stages)) # [3,4,2,1,5]

N = 4
stages = [4,4,4,4,4]
print(solution(N,stages)) # [4,1,2,3]
