def solution(n, money):
    money.sort(reverse=True)
    dp = [0] * 111111
    dp[0] = 1
    for i in range(money[0], n+1, money[0]):
        dp[i] = 1
    for j in range(1, len(money)):
        for i in range(n+1):
            if i >= money[j]:
                dp[i] += dp[i-money[j]] % 1000000007
    return dp[n]

n = 5
money = [1, 2, 5]
print(solution(n, money)) # 4