n, m = map(int, input().split())
nums = [[] for _ in range(n)]
for i in range(n):
    nums[i] = list(map(int, input().split()))

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    ans = 0
    for n in range(i-1, x):
        for m in range(j-1, y):
           ans += nums[n][m]
    print(ans)