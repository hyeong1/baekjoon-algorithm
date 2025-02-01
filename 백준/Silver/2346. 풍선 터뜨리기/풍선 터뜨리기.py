import sys
from collections import deque

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
idx = deque(i for i in range(n))
res = []

while True:
    now = idx.popleft()
    res.append(now + 1)
    if not idx:
        break
    move = arr[now]
    if move > 0:
        idx.rotate(-(move - 1))
    else:
        idx.rotate(-move) # popleft 후 원래 자리로 이동시키기 위해 -1 하지 않음

sys.stdout.write(" ".join(map(str, res)))