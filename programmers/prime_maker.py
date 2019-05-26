from itertools import combinations


def solution(nums):
    answer = 0
    nums.sort()
    max_sum = nums[-1] + nums[-2] + nums[-3]
    is_prime_ary = [True] * (max_sum + 1)
    for idx in range(2, max_sum):
        target = is_prime_ary[idx]
        if target:
            for idx2 in range(1, (max_sum // idx) + 1):
                if idx2 == 1:
                    continue
                is_prime_ary[idx * idx2] = False
    combs = combinations(nums, 3)
    for comb in combs:
        if is_prime_ary[sum(comb)]:
            answer += 1
    return answer


nums = [1, 2, 3, 4]
print(solution(nums))  # 1
nums = [1, 2, 7, 6, 4]
print(solution(nums))  # 4
