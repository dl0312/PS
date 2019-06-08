def solution(n, vertexs):
    graph = dict()
    for vertex in vertexs:
        if vertex[0] not in graph.keys():
            graph[vertex[0]] = set([vertex[1]])
        else: graph[vertex[0]].add(vertex[1])
        if vertex[1] not in graph.keys():
            graph[vertex[1]] = set([vertex[0]])
        else: graph[vertex[1]].add(vertex[0])
    queue = [[0,1]]
    visited = set()
    depths = [0,0]
    while queue:
        temp = queue.pop(0)
        depth = temp[0]
        n = temp[1]
        if n not in visited:
            visited.add(n)
            if depth + 1 != depths[0]:
                depths = [depth+1, len(visited)-1]
            for i in graph[n] - set(visited):
                queue.append([depth+1, i])
    return len(visited)-depths[1]

n = 6
vertexs = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2],[1,7]]
print(solution(n, vertexs)) # 3