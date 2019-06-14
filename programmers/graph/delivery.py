import sys

def solution(N, roads, K):
    graph = {}
    roads.sort()
    for road in roads:
        start, end, cost = road
        if start not in graph.keys():
            graph[start] = {end: cost}
        else:
            if end not in graph[start].keys():
                graph[start][end] = cost
            else:
                if graph[start][end] > cost:
                    graph[start][end] = cost
        end, start, cost = road
        if start not in graph.keys():
            graph[start] = {end: cost}
        else:
            if end not in graph[start].keys():
                graph[start][end] = cost
            else:
                if graph[start][end] > cost:
                    graph[start][end] = cost
    distance_list = {}
    for i in range(1, N+1):
        distance_list[i] = sys.maxsize
    distance_list[1] = 0
    stack = [1]
    while stack:
        current_node = stack.pop()
        for key in graph[current_node].keys():
            if distance_list[key] > distance_list[current_node] + graph[current_node][key]:
                distance_list[key] = distance_list[current_node] + graph[current_node][key]
                stack.append(key)
    answer = 0
    for value in distance_list.values():
        if value <= K:
            answer += 1
    return answer

N = 5
roads = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, roads, K)) # 4
N = 6
roads = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4
print(solution(N, roads, K)) # 4
