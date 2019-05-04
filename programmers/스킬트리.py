def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        last_skill_idx = -2
        for item in skill:
            cur_skill_idx = skill_tree.find(item)
            if last_skill_idx == -1:
                if cur_skill_idx != -1:
                    break
            elif last_skill_idx != -2 and last_skill_idx != -1:
                if cur_skill_idx <= last_skill_idx and cur_skill_idx != -1:
                    break
            last_skill_idx = cur_skill_idx
        else:
            answer += 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))