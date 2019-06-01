def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    print(shortest)
    return shortest

def similarity(str1, str2):
    result = 0
    for idx in range(len(str1)):
        if str1[idx] == str2[idx]:
            result += 1
    return result

def solution(begin, target, words):
    graph = {}
    l_word = len(begin)
    lst = []
    if target not in words:
        return 0
    for word in words:
        if similarity(begin, word) == l_word -1:
            lst.append(word)
    graph[begin] = lst
    for word1 in words:
        lst = []
        for word2 in words:
            if similarity(word1, word2) == l_word -1:
                lst.append(word2)
        graph[word1] = lst
    short_path = find_shortest_path(graph, begin, target)
    print(graph)
    if short_path:
        return len(short_path)-1
    else: return 0

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words)) # 4
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words)) # 0
begin = "hit"
target = "cog"
words = ["hot", "dot", "lot", "coc", "cog"]
print(solution(begin, target, words)) # 0