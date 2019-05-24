def solution(t_lst):
    t_lst_sorted = sorted(t_lst, reverse=True)
    t_len = len(t_lst)
    winter_max_t = t_lst[0]
    winter_max_t_idx = 0
    for idx, t in enumerate(t_lst):
        if t >= winter_max_t:
            winter_max_t_idx = t_lst_sorted.index(t)
        if t_len - winter_max_t_idx == idx+1:
            return idx + 1
