X = input()
res = 0

if X[0] != '0':
    res = int(X)
elif X[1] != 'x':
    nums = list(map(int, X[1:]))
    nums.reverse()
    for i in range(len(nums)):
        res += nums[i] * (8**i)
else:
    nums = list(map(str, X[2:]))
    nums.reverse()
    for i in range(len(nums)):
        if nums[i].isdigit():
            res += int(nums[i]) * (16**i)
        else:
            res += (int(ord(nums[i])) - 87) * (16**i)

print(res)
