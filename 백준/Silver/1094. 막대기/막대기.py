x = int(input())

sticks = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in range(7):
    if (x & (1 << i)) > 0:  # i번째 비트가 1인지 확인
        count += 1

print(count)
