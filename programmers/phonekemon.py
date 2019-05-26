def solution(nums):
    poke_set = set()
    for num in nums:
        poke_set.add(num)
    if len(poke_set) < len(nums) // 2:
        return len(poke_set)
    else: return len(nums)//2

nums = [3,1,2,3]
print(solution(nums)) # 2