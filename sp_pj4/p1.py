N = int(input())
A = input()
A = [int(n) for n in A.split(" ")]
print(A)
result = []
for idx in range(N):
    result.append(0)
for counter in A:
    if 1 <= counter and counter <= N:
        result[counter-1] += 1
    elif counter == N+1:
        max_counter = max(result)
        for idx in range(N):
            result[idx] = max_counter
print(" ".join([str(i) for i in result]))



