import sys
from collections import deque

N, d, k, c = map(int, sys.stdin.readline().split())
table = [int(sys.stdin.readline()) for _ in range(N)]

count = 0
start = 0
end = start + k
while start < N:
    check = table[start:end] + [c]
    if end >= N:
        end %= N
        check += table[:end]
    if count < len(set(check)):
        count = len(set(check))
    start += 1
    end = start + k

print(count)