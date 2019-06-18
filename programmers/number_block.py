from math import sqrt

def solution(begin, end):
    result = []
    if begin == 1:
        result.append(0)
        begin += 1
    for i in range(begin, end + 1):
        for j in range(2, int(sqrt(end) + 1)):
            if i % j == 0:
                result.append(i // j)
                break
        else:
            result.append(1)
    return result

begin = 1
end = 10
print(solution(begin, end)) # [0,1,1,2,1,3,1,4,3,5]

begin = 2
end = 10
print(solution(begin, end)) # [1,1,2,1,3,1,4,3,5]

begin = 6
end = 6
print(solution(begin, end)) # [3]
begin = 10000
end = 11000
print(solution(begin, end)) # [1,3]

# begin = 1
# end = 1000
# print(solution(begin, end)) # [0,1,1,2,1,3,1,4,3,5]