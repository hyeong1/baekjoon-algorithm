import sys

left = list(sys.stdin.readline().rstrip())
right = []

for _ in range(int(sys.stdin.readline())):
    c = sys.stdin.readline()
    if c[0] == 'L' and left:
        right.append(left.pop())
    elif c[0] == 'D' and right:
        left.append(right.pop())
    elif c[0] == 'B' and left:
        left.pop()
    elif c[0] == 'P':
        left.append(c[2])

left.extend(reversed(right))
print(''.join(left))
