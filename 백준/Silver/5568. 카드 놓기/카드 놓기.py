n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
check = [False] * n
result = []


def pick_card(path, level, picked):
    if level == k:
        result.append(path)
        return
    for i in range(n):
        if not check[i]:
            check[i] = True
            new_str = path + cards[i]
            pick_card(new_str, level+1, picked)
            check[i] = False


pick_card("", 0, check)
print(len(set(result)))