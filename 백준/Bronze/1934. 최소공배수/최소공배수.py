import sys

sys.setrecursionlimit(100000)

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split(" "))
    print((n* m) // gcd(n, m))