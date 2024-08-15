N = int(input())

for i in range(1, N+1):
    i_digit_sum = sum(map(int, str(i)))
    resolve_sum = i + i_digit_sum
    if resolve_sum == N:
        print(i)
        break
    elif i == N:
        print(0)
        break
