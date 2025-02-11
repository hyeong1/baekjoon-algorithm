n, m = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
sums = []
for i in range(n):
    if i == 0:
        sums.append(nums[i])
    else:
        sums.append(sums[i-1] + nums[i])

for _ in range(m):
    i, j = map(int, input().split(" "))
    if i - 1 == 0:
        print(sums[j - 1])
    else:
        print(sums[j - 1] - sums[i-2])