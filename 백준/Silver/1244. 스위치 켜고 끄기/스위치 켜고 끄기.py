n = int(input())
states = [0]
switch = list(map(int, input().split()))
for s in switch:
    if s == 1:
        states.append(True)
    else:
        states.append(False)

t = int(input())
for _ in range(t):
    s, x = map(int, input().split())
    if s == 1:
        for i in range(x, n+1):
            if i % x == 0:
                states[i] = not states[i]
    else:
        left, right = x-1, x+1
        while left > 0 and right < n+1:
            if states[left] != states[right]:
                break
            left -= 1
            right += 1
        for i in range(left+1, right):
            states[i] = not states[i]

for i in range(1, n+1):
    if states[i]:
        print(1, end=" ")
    else:
        print(0, end=" ")
    if i % 20 == 0:
        print()