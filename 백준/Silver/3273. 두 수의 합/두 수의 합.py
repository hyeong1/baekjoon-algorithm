import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(" ")))
x = int(sys.stdin.readline())
start, end = 0, n-1
ans = 0
nums.sort()
while start < n-1:
    sum = nums[start] + nums[end]
    if sum >= x:
        end -= 1
        if sum == x:
            ans += 1
    elif sum < x:
        start += 1
        end = n-1
    if start == end:
        break
print(ans)