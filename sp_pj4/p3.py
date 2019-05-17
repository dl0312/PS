def solution(A):
    ary = []
    for a in A:
        for b in A:
            ary.append(abs(a+b))
    ary.sort()
    return ary[0]

input = [int(i) for i in input().split(" ")]
print(solution(input))