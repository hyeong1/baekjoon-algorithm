import sys

n = int(sys.stdin.readline())
nums = set(map(int, sys.stdin.readline().split(" ")))
print(*sorted(nums))