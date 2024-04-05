import sys

N, M = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()

for _ in range(M):
    target = int(sys.stdin.readline())
    start = 0
    end = N - 1
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            if end == mid:  # lower_bound
                break
            end = mid
        elif target > nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            end = mid - 1

    if nums[mid] == target:
        print(mid)
    else:
        print(-1)
