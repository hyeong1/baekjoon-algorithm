import sys

T = int(input())
k = int(input())
dp = [0] * (T+1)
dp[0] = 1

coins = []
for _ in range(k):
    value, count = map(int, sys.stdin.readline().split())
    coins.append([value, count])

for value, count in coins:
    for target in range(T, -1, -1):
        cnt = 1
        while cnt <= count and target - (value * cnt) >= 0:
            dp[target] = dp[target - (value * cnt)] + dp[target]
            cnt += 1

print(dp[T])
