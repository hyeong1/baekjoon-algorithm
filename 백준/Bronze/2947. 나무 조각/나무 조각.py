nums = list(map(int, input().split()))

while nums != sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp
            print(*nums)