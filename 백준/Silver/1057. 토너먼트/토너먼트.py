n, j, h = map(int, input().split(" "))
ans = 0

while j != h:
    j -= j // 2
    h -= h // 2
    ans += 1

print(ans)