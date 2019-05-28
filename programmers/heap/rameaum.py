# use heapq for heap
import heapq

def solution(stock, dates, supplies, k):
    answer = 0  # answer
    last_idx = 0    # save last index of dates & supplies
    pq = [] # priority queue list
    while stock < k:
        for idx in range(last_idx, len(dates)):
            if dates[idx] <= stock:
                heapq.heappush(pq, -supplies[idx])  # push minus data for max heap
                last_idx = idx + 1  # update last index
            else:
                break   # if date is not a proper candidate break for loop
        stock -= heapq.heappop(pq)  # max heap pop
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
