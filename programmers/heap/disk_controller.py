import heapq

def solution(jobs):
    prev = -1
    curr = 0
    heap = []
    length = len(jobs)
    answer = 0
    count = 0
    while count < length:
        for job in jobs:
            if prev < job[0] <= curr:
                answer += (curr - job[0])
                heapq.heappush(heap, job[1])
        if heap:
            answer += len(heap)*heap[0]
            prev = curr
            curr += heapq.heappop(heap)
            count += 1
        else:
            curr += 1
    return answer//length

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs)) # 9
jobs = [[0, 3], [4, 4], [2, 6]]
print(solution(jobs)) # 6 3, 7, 9  3, 4, 12
