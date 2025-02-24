t = int(input())

ans = list(input())
for _ in range(t - 1):
    n = input()
    for i in range(len(ans)):
        if ans[i] == n[i]:
            continue
        ans[i] = '?'
print("".join(ans))