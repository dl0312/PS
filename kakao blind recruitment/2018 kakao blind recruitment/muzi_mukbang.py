def solution(food_times, k):
    s_times = sorted(food_times)
    l_times = len(food_times)
    d_time = 0
    l_idx = 0
    for idx in range(l_times):
        if idx == 0:
            d_time += s_times[idx]*(l_times - idx)
        else:
            d_time += (s_times[idx]-s_times[idx-1])*(l_times - idx)
        if d_time > k:
            l_idx = idx -1
            break
    if d_time <= k:
        return -1
    lst = []
    for idx in range(l_times-1, -1, -1):
        if food_times[idx] > s_times[l_idx]:
            lst.append(idx+1)
    if len(lst) != 0:
        # 초과한 양만큼 뒤에서 순서를 세서 음식을 구합니다.
        return lst[(d_time - k -1) % len(lst)]
    else:
        # 모든 음식의 번호가 같은 경우, 전체에서 나머지 연산을 해서 결과를 구합니다.
        return k % l_times+1

food_time = [3, 1, 2]
k = 5
print(solution(food_time, k)) # 1
food_time = [3, 1, 3]
k = 6
print(solution(food_time, k)) # 3
food_time = [2, 2, 2]
k = 5
print(solution(food_time, k)) # 3
