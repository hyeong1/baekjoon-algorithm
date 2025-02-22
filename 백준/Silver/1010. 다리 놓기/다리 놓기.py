t = int(input())

for _ in range(t):
    n, m = map(int, input().split(" "))
    mm = 1
    nn = 1
    for i in range(1, m+1):
        mm *= i
    for i in range(1, n+1):
        nn *= i
    for i in range(1, (m-n)+1):
        nn *= i
    print(mm // nn)