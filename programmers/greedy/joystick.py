def solution(name):
    answer = 0
    name = list(name)
    base = ['A'] * len(name)
    idx = 0
    while True:
        r_idx = 1
        l_idx = 1
        if name[idx] != 'A':
            if ord(name[idx]) - ord('A') > 13:
                answer += 26 - (ord(name[idx]) - ord('A'))
            else:
                answer += ord(name[idx]) - ord('A')
            name[idx] = 'A'
        if name == base:
            break
        else:
            print(name)
            for i in range(1, len(name)):
                print(idx+i)
                if name[idx + i] == 'A':
                    r_idx += 1
                else:
                    break
                if name[idx - i] == 'A':
                    l_idx += 1
                else:
                    break
            if r_idx > l_idx:
                answer += l_idx
                idx -= l_idx
            else:
                answer += r_idx
                idx += r_idx
    return answer


name = "JEROEN"
print(solution(name))  # 56
name = "JAN"
print(solution(name))  # 23
name = "Z"
print(solution(name))  # 1
name = "AA"
print(solution(name))  # 0
name = "AZ"
print(solution(name))  # 2
name = "ABA"
print(solution(name))  # 2
name = "ABABAAAAAAABA"
print(solution(name))  # 10
