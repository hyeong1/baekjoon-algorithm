def max_candy(arr, n):
    _max = 0
    # 행
    count = 1
    for i in range(n):
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1]:
                count += 1
                _max = max(_max, count)
            else:
                count = 1
        count = 1
    # 열
    count = 1
    for i in range(n):
        for j in range(n-1):
            if arr[j][i] == arr[j+1][i]:
                count += 1
                _max = max(_max, count)
            else:
                count = 1
        count = 1
    return _max


n = int(input())
candy = []
result = 0
for _ in range(n):
    candy.append(list(input()))

for i in range(n):
    for j in range(n-1):
        if candy[i][j] != candy[i][j+1]:
            temp = candy[i][j]
            candy[i][j] = candy[i][j+1]
            candy[i][j+1] = temp
            result = max(result, max_candy(candy, n))
            temp = candy[i][j]
            candy[i][j] = candy[i][j+1]
            candy[i][j+1] = temp

for i in range(n):
    for j in range(n-1):
        if candy[j][i] != candy[j+1][i]:
            temp = candy[j][i]
            candy[j][i] = candy[j+1][i]
            candy[j+1][i] = temp
            result = max(result, max_candy(candy, n))
            temp = candy[j][i]
            candy[j][i] = candy[j+1][i]
            candy[j+1][i] = temp

print(result)