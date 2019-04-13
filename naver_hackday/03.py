from collections import Counter

def solution(t_lst):
    t_lst_sorted = sorted(t_lst, reverse = True)
    winter_max_t = t_lst[0]
    winter_max_t_idx = 0
    for idx, t in enumerate(t_lst):
        if t >= winter_max_t:
            winter_max_t_idx = t_lst_sorted.index(t)
        if Counter(t_lst_sorted[winter_max_t_idx:]) == Counter(t_lst[:idx+1]):
            return idx+1