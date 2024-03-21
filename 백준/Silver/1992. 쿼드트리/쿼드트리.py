n = int(input())
total = [input() for _ in range(n)]
int_map = []

for row in total:
    s_to_i = [int(c) for c in row]
    int_map.append(s_to_i)


def quad_tree(size, x, y):
    check = 0
    for i in range(y, y + size):
        for j in range(x, x + size):
            check += int_map[i][j]
    if check == 0:
        print("0", end="")
        return
    if check == size * size:
        print("1", end="")
        return
    else:
        size //= 2
        print("(", end="")
        quad_tree(size, x, y)
        quad_tree(size, x + size, y)
        quad_tree(size, x, y + size)
        quad_tree(size, x + size, y + size)
        print(")", end="")
        return


quad_tree(n, 0, 0)
