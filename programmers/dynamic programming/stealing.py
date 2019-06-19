def solution(houses):
    length = len(houses)
    dp_with_first = [0]*(length-1)
    dp_without_first = [0]*length
    dp_with_first[0] = houses[0]
    dp_with_first[1] = houses[0]
    dp_without_first[0] = 0
    dp_without_first[1] = houses[1]

    for i in range(2, length-1):
        dp_with_first[i] = max(dp_with_first[i-2] + houses[i], dp_with_first[i-1])
    for i in range(2, length):
        dp_without_first[i] = max(dp_without_first[i-2] + houses[i], dp_without_first[i-1])

    return max(dp_with_first[length-2], dp_without_first[length-1])

money = [1,2,3,1]
print(solution(money)) # 4
# money = [1,2,3]
# print(solution(money)) # 4