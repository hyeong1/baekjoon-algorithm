from collections import deque

n, k = map(int, input().split(" "))
dq = deque([str(i) for i in range(1, n+1)])
res = []

while len(dq) > 1:
    dq.rotate(-(k-1))
    res.append(dq.popleft())

res.append(dq.pop())
print("<" + ", ".join(res) + ">")