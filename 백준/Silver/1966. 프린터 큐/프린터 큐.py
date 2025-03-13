from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().split(" "))
    ll = list(map(int, input().split(" ")))
    dq = []
    for i in range(n):
        dq.append([i, ll[i]])
    dq = deque(dq)
    _max = max(dq, key=lambda x : x[1])[1]
    
    res = []
    while dq:
        now = dq[0]
        if now[1] < _max:
            dq.rotate(-1)
        elif now[1] == _max:
            res.append(dq.popleft())
            if len(dq) == 0:
                break
            _max = max(dq, key=lambda x: x[1])[1]
    
    for i in range(n):
        if res[i][0] == k:
            print(i+1)
            break
