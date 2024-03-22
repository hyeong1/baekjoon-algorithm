import sys
t = int(input())
tops = list(map(int, sys.stdin.readline().split()))
stack = []
check = [0] * t

answer = [0] * t
for i in range(t-1, -1, -1):
    if not stack:
        stack.append([i, tops[i]])
        continue
    if tops[i] > stack[-1][1]:
        while stack and tops[i] > stack[-1][1]:
            answer[stack[-1][0]] = i + 1
            stack.pop()
        stack.append([i, tops[i]])
    if tops[i] < stack[-1][1]:
        stack.append([i, tops[i]])

for c in answer:
    print(c, end=" ")