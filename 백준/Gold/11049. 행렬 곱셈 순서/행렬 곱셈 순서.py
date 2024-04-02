import sys

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[float("inf")] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 0

for term in range(1, N): 
    for i in range(N):
        if i + term == N:
            break
        for j in range(i, i+term):
            dp[i][i+term] = min(dp[i][i+term],
                                dp[i][j] + dp[j+1][i+term] + (matrix[i][0] * matrix[j+1][0] * matrix[i+term][1]))

print(dp[0][-1])
