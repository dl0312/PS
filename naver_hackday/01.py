def solution(pips):
    dice = [1, 6, 2, 5, 3, 4]
    dice_lst1 = {1: 0, 6: 0, 2: 0, 5: 0, 3: 0, 4: 0}
    dice_lst2 = [0, 0, 0]
    for pip in pips:
        if pip is 1:
            dice_lst1[1] += 1
        elif pip is 6:
            dice_lst1[6] += 1
        elif pip is 2:
            dice_lst1[2] += 1
        elif pip is 5:
            dice_lst1[5] += 1
        elif pip is 3:
            dice_lst1[3] += 1
        elif pip is 4:
            dice_lst1[4] += 1
    dice_lst2[0] = dice_lst1[1] - dice_lst1[6]
    dice_lst2[1] = dice_lst1[2] - dice_lst1[5]
    dice_lst2[2] = dice_lst1[3] - dice_lst1[4]
    print(dice_lst1, dice_lst2)
    m_idx = [abs(i) for i in dice_lst2].index(max([abs(i) for i in dice_lst2]))
    if dice_lst2[m_idx] > 0:
        target_pip = dice[m_idx*2]
    else:
        target_pip = dice[m_idx*2 + 1]
    rotate_ctr = 0
    for key in dice_lst1.keys():
        if key == target_pip:
            continue
        elif key == 7-target_pip:
            rotate_ctr += 2*dice_lst1[key]
        else:
            rotate_ctr += dice_lst1[key]

    return rotate_ctr