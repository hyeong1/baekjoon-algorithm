n, m = map(int, input().split())
nums = [list(str(input())) for _ in range(n)]
result = 1

for i in range(n):
    for j in range(m):
        k = 1
        q = 0
        while i + q < n and j + q < m:
            if nums[i][j] == nums[i][j+q] == nums[i+q][j] == nums[i+q][j+q]:
                k = 1 + q
            q += 1
        result = max(result, k)

print(result*result)