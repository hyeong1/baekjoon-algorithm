n = int(input())
ans = []

for m in range(n):
    nums = list(map(int, input().split()))
    visited = [False] * 5
    _max = 0
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                res = (nums[i] + nums[j] + nums[k]) % 10
                if _max < res:
                    _max = res
    ans.append(_max)

ans.reverse()
print(n - ans.index(max(ans)))