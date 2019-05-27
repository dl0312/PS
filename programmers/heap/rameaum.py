import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    idx = 0
    h = []
    while (stock < k):
        for i in range(idx, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(h, (-supplies[i], supplies[i]))
                idx = i + 1
            else:
                break
        stock += heapq.heappop(h)[1]
        answer += 1
    return answer

stock = 4
dates = [4, 10, 15]
supplies = [20, 5, 10]
k = 30
print(solution(stock, dates, supplies, k))  # 2
stock = 4
dates = [4, 9, 10]
supplies = [5, 5, 10]
k = 19
print(solution(stock, dates, supplies, k))  # 3
stock = 10
dates = [1, 2, 3]
supplies = [5, 5, 10]
k = 9
print(solution(stock, dates, supplies, k))  # 0
