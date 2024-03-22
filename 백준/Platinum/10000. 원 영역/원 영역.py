import sys

N = int(input())
circles = []
for _ in range(N):
    center, radius = map(int, sys.stdin.readline().split())
    left = ["L", center - radius]
    right = ["R", center + radius]
    circles.append(left)
    circles.append(right)
circles.sort(key=lambda x: x[0], reverse=True)  # R이 L보다 먼저 오도록 정렬
circles.sort(key=lambda x: x[1])

answer = 1  # 밖 영역
stack = []
for c in circles:
    if c[0] == "L":
        stack.append(c)
        continue

    total_width = 0
    while stack:
        prev = stack.pop()
        if prev[0] == "L":
            width = c[1] - prev[1]
            if total_width == width:
                answer += 2
            else:
                answer += 1
            stack.append(["C", width])
            break
        elif prev[0] == "C":
            total_width += prev[1]

print(answer)