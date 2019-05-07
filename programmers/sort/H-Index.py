def solution(citations):
    citations.sort( reverse=True)
    for idx in range(len(citations)):
        if citations[idx] >= idx+1:
            continue
        else:
            idx -= 1
            break
    return idx + 1

citations = [3, 0, 6, 1, 5]
print(solution(citations))

citations = [5, 5, 5, 5, 5]
print(solution(citations))