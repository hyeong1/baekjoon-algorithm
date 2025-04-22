from collections import deque

n = int(input())
li = deque([i for i in range(1, n+1)])
out = []

while li:
    out.append(li.popleft())
    li.rotate(-1)

print(*out)