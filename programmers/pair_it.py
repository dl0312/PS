def solution(s):
    stack = []
    for c in s:
        if not stack:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return int(not(stack))

s = "baabaa"
print(solution(s))  # 1
s = "cdcd"
print(solution(s))  # 0
s = "baaabaaa"
print(solution(s))  # 0
s = "baaaabaaaa"
print(solution(s))  # 1
s = "baa" *300000
print(solution(s))
