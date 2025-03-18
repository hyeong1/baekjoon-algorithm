num = input()
ans = 1
sets = {}
for i in range(10):
    sets[i] = 1

for n in num:
    n_int = int(n)
    if sets[n_int] > 0:
        sets[n_int] -= 1
    else:
        if n_int == 9 and sets[6] > 0:
            sets[6] -= 1
        elif n_int == 6 and sets[9] > 0:
            sets[9] -= 1
        else:
            ans += 1
            for i in range(10):
                if i != n_int:
                    sets[i] += 1

print(ans)