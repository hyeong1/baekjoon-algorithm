n = int(input())

if n == 0:
    print(0)
    exit()
if n < 3:
    print(1)
    exit()

dp = [0] * (n+1)
dp[1] = 1
dp[2] = 1

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])