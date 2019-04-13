def get_opposite(pip):
    return 7 - pip

def solution(pips):
    dice_lst = [1, 6, 2, 5, 3, 4]
    dice_dict = {1: 0, 6: 0, 2: 0, 5: 0, 3: 0, 4: 0}
    dice_pair_lst = [0, 0, 0]

    for pip in pips:
        dice_dict[pip] += 1
    for i in range(3):
        dice_pair_lst[i] = dice_dict[i+1] - dice_dict[get_opposite(i+1)]
    m_idx = [abs(i) for i in dice_pair_lst].index(max([abs(i) for i in dice_pair_lst]))
    if dice_pair_lst[m_idx] > 0:
        target_pip = dice_lst[m_idx*2]
    else:
        target_pip = dice_lst[m_idx*2 + 1]
    rotate_ctr = 0
    for key in dice_dict.keys():
        if key == target_pip:
            continue
        elif key == 7-target_pip:
            rotate_ctr += 2*dice_dict[key]
        else:
            rotate_ctr += dice_dict[key]
    return rotate_ctr

print(solution([1,2,3]))