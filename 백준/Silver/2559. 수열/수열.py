n, m = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
sums = []
for i in range(n):
    if i == 0:
        sums.append(nums[i])
    else:
        sums.append(sums[i-1] + nums[i])

res = float("-inf")
i = 0
for j in range(m-1, n):
    if i == 0:
        res = max(res, sums[j])
    else:
        res = max(res, sums[j] - sums[i-1])
    i += 1
print(res)