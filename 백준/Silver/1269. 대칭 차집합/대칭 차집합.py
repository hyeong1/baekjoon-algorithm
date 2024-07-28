len_a, len_b = map(int, input().split())
a = list(map(int, input().split()))
a_dict = {value: i for i, value in enumerate(a)}
b = list(map(int, input().split()))
b_dict = {value: i for i, value in enumerate(b)}
res = 0

for key in a_dict:
    if key not in b_dict:
        res += 1

for key in b_dict:
    if key not in a_dict:
        res += 1

print(res)
