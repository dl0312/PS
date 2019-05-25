def solution(s):
    words = s.split(" ")
    for idx in range(len(words)):
        words[idx] = words[idx].lower()
        words[idx] = words[idx][:1].upper() + words[idx][1:]
    answer = 0
    return " ".join(words)

s = "3people unFollowed me"
print(solution(s)) # 3people Unfollowed Me
s = "for the last week"
print(solution(s)) # For The Last Week
