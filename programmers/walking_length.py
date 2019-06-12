def solution(dirs):
    dirs = list(dirs)
    arrow_key = {'U': [0,1], 'R': [1,0], 'D': [0,-1], 'L': [-1,0]}
    ways = set()
    curr_pos = [0,0]
    for dir in dirs:
        next_pos = [sum(x) for x in zip(curr_pos, arrow_key[dir])]
        middle_pos = [x[0] + x[1]/2 for x in zip(curr_pos, arrow_key[dir])]
        print(ways)
        if abs(next_pos[0]) <= 5 and abs(next_pos[1]) <= 5:
            if middle_pos[0] + middle_pos[1]*6 not in ways:
                ways.add(middle_pos[0] + middle_pos[1]*6)
            curr_pos = next_pos
    answer = len(ways)
    return answer

dirs = "ULURRDLLU"
print(solution(dirs)) # 7
dirs = "LULLLLLLU"
print(solution(dirs)) # 7
dirs = "U"
print(solution(dirs)) # 1
dirs = "UDUDUD"
print(solution(dirs)) # 1
