n = int(input())
nums = {}
nums_array = []

for _ in range(n):
    k = int(input())
    nums_array.append(k)
    if k in nums:
        nums[k] += 1
    else:
        nums[k] = 1

print(round(sum(nums_array) / n))
print(sorted(nums_array)[n // 2])
max_cnt = max(nums.values())
chk = []
for k, v in nums.items():
    if v == max_cnt:
        chk.append(k)
if len(chk) == 1:
    print(*chk)
else:
    print(sorted(chk)[1])
print(max(nums) - min(nums))