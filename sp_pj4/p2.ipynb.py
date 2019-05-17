def prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

A = [int(i) for i in input().split(" ")]
B = [int(i) for i in input().split(" ")]
result = 0
for idx in range(len(A)):
    if prime_factors(A[idx]) == prime_factors(B[idx]):
        result += 1
print(result)

