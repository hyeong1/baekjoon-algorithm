import sys

N, K = map(int, sys.stdin.readline().split())

gold, silver, bronze = [0] * (N+1), [0] * (N+1), [0] * (N+1)
medals = {}
for i in range(N):
    idx, g, s, b = map(int, sys.stdin.readline().split())
    medals[idx] = (g, s, b)

K_medals = medals[K]

cnt = 1
for n, n_medals in medals.items():
    if n != K:
        if n_medals > K_medals:
            cnt += 1

print(cnt)
