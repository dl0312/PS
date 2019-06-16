def solution(n):
    count = 0
    for i in range(n):  # 첫 행의 경우의 수
        stack = [[i]]
        while stack:
            curr_sol = stack.pop()
            len_curr_sol = len(curr_sol)
            if len_curr_sol == n:  # 정답 배열(sol)의 길이가 n과 같아지면, count 증가
                count += 1
            candidate = list(range(n))  # 0부터 n-1까지를 후보 배열로 만든다.
            for i in range(len_curr_sol):
                if curr_sol[i] in candidate:  # 같은 열에 있는 지 확인
                    candidate.remove(curr_sol[i])  # 같은 열에 있다면 후보에서 제외
                distance = len(curr_sol) - i
                if curr_sol[i] + distance in candidate:  # 같은 대각성 상(+)에 있는 지 확인
                    candidate.remove(curr_sol[i] + distance)  # 같은 대각선 상에 있다면 후보에서 제외
                if curr_sol[i] - distance in candidate:  # 같은 대각선 상(-)에 있는 지 확인
                    candidate.remove(curr_sol[i] - distance)  # 같은 대각선 상에 있다면 후보에서 제외
            if candidate:
                for i in candidate:
                    temp_sol = curr_sol[:]
                    temp_sol.append(i)
                    stack.append(temp_sol)
    return count

N = 4
print(solution(N)) # 2