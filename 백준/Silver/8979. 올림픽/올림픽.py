import sys

N, K = map(int, sys.stdin.readline().split())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

info.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
for i in range(N-1):
    if info[i][0] == K:
        print(i)
        break
