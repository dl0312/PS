def solution(number, k):
    length = len(number)
    if length > k:
        m = 0
        for cnt in range(k):
            for idx in range(m, length-1):
                if number[idx] < number[idx+1]:
                    number = number[:idx] + number[idx+1:]
                    length -= 1
                    if idx > 0:
                        m = idx-1
                    break
            else:
                number = number[:length-k+cnt]
                break
        return "".join([str(i) for i in number])
    else:
        return "0"

number = "1924"
k = 2
print(1, solution(number, k))
number = "1231234"
k = 3
print(2, solution(number, k))
number = "4177252841"
k = 4
print(3, solution(number, k))
number = "22222"
k = 4
print(4, solution(number, k))
number = "1111"
k = 4
print(5, solution(number, k))
number = "1234"
k = 4
print(6, solution(number, k))
number = "11000"
k = 4
print(7, solution(number, k))
number = "1234567890"
k = 9
print(8, solution(number, k))
number = "9"*1000000
k = 999999
print(9, solution(number, k))
number = "1234567890"*100000
k = 999999
print(10, solution(number, k))
number = "1234567890"*100000
k = 999999
print(10, solution(number, k))