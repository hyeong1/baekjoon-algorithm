import sys

N, K = map(int, input().split())
seq = list(map(int, sys.stdin.readline().split()))

use = []
cnt = 0
for i in range(K):
    if seq[i] not in use:
        if len(use) < N:
            use.append(seq[i])
            continue
        again = []
        for u in use:
            if u in seq[i:]:
                again.append(seq[i:].index(u))
            else:
                again.append(float('inf'))
        out = again.index(max(again))
        use.remove(use[out])
        use.append(seq[i])
        cnt += 1

print(cnt)
