import heapq

def solution(scoville, K):
    heap = []
    cnt = 0
    for info in scoville:
        heapq.heappush(heap, info)
    while heap[0] < K:
        min = heapq.heappop(heap)
        second_min = heapq.heappop(heap)
        heapq.heappush(heap, min + second_min*2)
        cnt += 1
    return cnt

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))