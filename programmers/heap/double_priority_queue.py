def solution(operations):
    pq = []
    for operation in operations:
        if operation[0] == 'I':
            item = int(operation.split(" ")[1])
            pq.append(item)
            pq.sort()
        elif operation[0] == 'D':
            option = int(operation.split(" ")[1])
            if option == 1:
                if pq:
                    pq.remove(max(pq))
            elif option == -1:
                if pq:
                    pq.remove(min(pq))
    if not pq:
        return [0, 0]
    else:
        return [pq[-1], pq[0]]

operations = ["I 16", "D 1"]
print(solution(operations)) # [0,0]
operations = ["I 7", "I 5", "I -5", "D -1"]
print(solution(operations)) # [7,5]
operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations)) # [0,0]
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations)) # [333,-45]
operations = ["I 16", "I 16", "D 1"]
print(solution(operations)) # [16,16]
operations = ["D 1"]
print(solution(operations)) # [0,0]
