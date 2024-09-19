import sys

N = int(sys.stdin.readline())
sg = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

for c in cards:
    if c in sg:
        print('1', end=" ")
    else:
        print('0', end=" ")
