n = int(input())
dp = [0 for _ in range(n)]

dp[0] = 1
for i in range(2, n):
    dp[i] = dp[i - 2]

if dp[-1] == 1:
    print('SK')
else:
    print('CY')