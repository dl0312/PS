def solution(n, arr1, arr2):
    answer = []
    for dec1, dec2 in zip(arr1, arr2):
        bin12 = bin(dec1|dec2)[2:]
        bin12 = '0' * (n-len(bin12)) + bin12
        bin12 = bin12.replace('1', '#')
        bin12 = bin12.replace('0', ' ')
        answer.append(bin12)
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2)) # ["#####","# # #", "### #", "# ##", "#####"]