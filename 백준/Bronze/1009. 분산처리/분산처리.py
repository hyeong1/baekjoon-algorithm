t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = 1
    a = a % 10

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % 10
        a = (a * a) % 10
        b //= 2
    print(10 if result == 0 else result)