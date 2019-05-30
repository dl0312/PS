def solution(s):
    longest_palindrome = 0
    table = [[False for i in range(len(s))] for j in range(len(s))]

    # 다음과 같은 방식으로 테이블을 생성합니다.
    for i in range(len(s)):
        for j in range(len(s) - i):
            # len(substring) < 3일 경우에는
            # substring의 끝이 같을 경우 True를 넣고, longest_palindrome을 업데이트합니다.
            if i < 2:
                if s[j] == s[i+j]:
                    table[j][i+j] = True
                    longest_palindrome = i+1
                else:
                    table[j][i+j] = False
            # len(substring) > 3일 경우
            # substring의 끝이 같고, 왼쪽 밑 대각선 한칸에 있는 박스가 True면 True를 넣고, longest_palindrome을 업데이트합니다.
            else:
                if s[j] == s[i+j] and table[j+1][i+j-1]:
                    table[j][i+j] = True
                    longest_palindrome = i+1
                else:
                    table[j][i+j] = False
    return longest_palindrome

s = "a"
print(solution(s)) # 1
s = "abcd"
print(solution(s)) # 1
s = "abcdcba"
print(solution(s)) # 7
s = "abacde"
print(solution(s)) # 3
s = "abaaba"
print(solution(s)) # 6
s = "caba"
print(solution(s)) # 3
s = "abbac"
print(solution(s)) # 4
s = "cabba"
print(solution(s)) # 4
