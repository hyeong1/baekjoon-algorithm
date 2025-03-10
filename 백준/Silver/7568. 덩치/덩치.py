n = int(input())
arr = []

for i in range(n):
    x, y = map(int, input().split(" "))
    arr.append([x, y])

for i in range(n):
    w1, h1 = arr[i]
    cnt = 1
    for j in range(n):
        if i != j:
            w2, h2 = arr[j]
            if w1 < w2 and h1 < h2:
                cnt += 1
    print(cnt, end=" ")