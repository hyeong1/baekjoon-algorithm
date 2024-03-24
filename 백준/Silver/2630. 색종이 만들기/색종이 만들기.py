paper = [[0] * 129] * 129
n = int(input())
white, blue = 0, 0

for i in range(n):
    paper[i] = list(map(int, input().split()))


def cut(size, x, y):
    global white, blue
    blue_check = 0
    for k in range(x, x + size):
        for j in range(y, y + size):
            if paper[k][j] == 1:
                blue_check += 1
    if blue_check == 0:
        white += 1
    elif blue_check == (size ** 2):
        blue += 1
    else:
        size //= 2
        cut(size, x, y)
        cut(size, x, y + size)
        cut(size, x + size, y)
        cut(size, x + size, y + size)


cut(n, 0, 0)
print(white)
print(blue)
