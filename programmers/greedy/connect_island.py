parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])

    return parent[v]

def union(v, u):
    root1 = find(v)
    root2 = find(u)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2

            if rank[root1] == rank[root2]:
                rank[root2] += 1

def solution(n, costs):
    graph = dict()
    mst = []
    graph['vertices'] = []
    graph['edges'] = costs
    graph['edges'].sort(key=lambda edge: edge[2])
    for cost in costs:
        f, t, c = cost
        if f not in graph['vertices']:
            graph['vertices'].append(f)
        if t not in graph['vertices']:
            graph['vertices'].append(t)
    graph['vertices'].sort()
    for v in graph['vertices']:
        make_set(v)
    for edge in graph['edges']:
        f, t, c = edge
        if find(f) != find(t):
            union(f,t)
            mst.append(edge)
    answer = 0
    for vertex in mst:
        answer += vertex[2]
    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs)) # 4