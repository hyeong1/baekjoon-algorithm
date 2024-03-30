string_a = ' ' + input()
string_b = ' ' + input()
len_a, len_b = len(string_a), len(string_b)
dp = [[0] * len_b for _ in range(len_a)]

for i in range(1, len_a):
    for j in range(1, len_b):
        if string_a[i] == string_b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len_a-1][len_b-1])

start_r, start_c = len_a - 1, len_b - 1
direction = [[-1, 0], [0, -1]]  # 위, 왼쪽 대각선, 왼쪽
stack = []
while start_r > 0 and start_c > 0:
    for dr, dc in direction:
        if dp[start_r + dr][start_c + dc] == dp[start_r][start_c]:
            start_r, start_c = start_r + dr, start_c + dc
            continue
    if string_a[start_r] == string_b[start_c]:
        stack.append(string_a[start_r])
        start_r -= 1
        start_c -= 1

for i in range(len(stack)-1, -1, -1):
    print(stack[i], end="")
