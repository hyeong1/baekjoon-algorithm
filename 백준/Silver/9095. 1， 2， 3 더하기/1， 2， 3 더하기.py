T = int(input())

for _ in range(T):
    N = int(input())
    if N == 1 or N == 2:
        print(N)
        continue
    if N == 3:
        print(4)
        continue

    dp = [1] * (N+1)
    dp[2] = 2
    dp[3] = 4

    for i in range(4, N+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    print(dp[N])
