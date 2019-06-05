def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    pivot_b = 0
    for idx_a in range(len(A)):
        for idx_b in range(pivot_b, len(B)):
            if B[idx_b] > A[idx_a]:
                pivot_b = idx_b + 1
                answer += 1
                break
    return answer
A = [5,1,3,7]
B = [2,2,6,8]
print(solution(A, B)) # 3
A = [5,1,3,7,3]
B = [2,4,6,8,2]
print(solution(A, B)) # 4
A = [2, 2, 2, 2]
B = [1, 1, 1, 1]
print(solution(A, B)) # 0
A = [2, 4, 4, 4]
B = [3, 1, 5, 5]
print(solution(A, B)) # 3