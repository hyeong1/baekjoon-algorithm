import sys

n, t, p = map(int, input().split())
if n == 0:
    print(1)
    sys.exit()

rank = list(map(int, input().split()))

if n == p and rank[-1] >= t:
    print(-1)
    sys.exit()

ans = 0
for i in range(n):
    if rank[i] <= t:
        ans = i + 1
        break
if ans == 0:
    ans = n + 1
print(ans)