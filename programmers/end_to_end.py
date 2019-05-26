def solution(n, words):
    answer = [0, 0]
    used = []
    people = [0] * n
    for idx, word in enumerate(words):
        if len(used) == 0:
            if len(word) <= 1:
                answer = [idx % n, people[idx % n + 1]]
                break
            else:
                used.append(word)
                people[idx % n] += 1
                continue
        if used[-1][-1] != word[0] or len(word) <= 1 or word in used:
            people[idx % n] += 1
            answer = [idx % n + 1, people[idx % n]]
            break
        else:
            used.append(word)
            people[idx % n] += 1
    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))
n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))