def DFS(T, path_set):
    if T.l != None:
        DFS(T.l, path_set | {T.l.x})
    if T.r != None:
        DFS(T.r, path_set | {T.r.x})
    if T.l == None and T.r == None:
        path_len_lst.append(len(path_set))

def solution(T):
    DFS(T, {T.x})
    return max(path_len_lst)