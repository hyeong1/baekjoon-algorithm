N = int(input())
i = 2
result = []

while i <= N:
    if N % i == 0:
        N /= i
        result.append(i)
    else:
        i += 1

for r in result:
    print(r)