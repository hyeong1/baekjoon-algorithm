import sys
t = int(input())
sticks = []
for i in range(t):
    sticks.append(int(sys.stdin.readline()))

count = 0
max_h = 0
for s in reversed(sticks):
    if s > max_h:
        count += 1
        max_h = s

print(count)