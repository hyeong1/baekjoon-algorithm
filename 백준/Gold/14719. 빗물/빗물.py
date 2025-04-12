h, w = map(int, input().split())
block = list(map(int, input().split()))

water = 0

# 1부터 시작해서 현재 좌우 최대 높이 구해서 'min(좌, 우) - 현재'가 고인 빗물양
# 빗물양을 한칸씩 찾아가기
for i in range(1, w-1):
    left, right = 0, 0
    for j in range(i, -1, -1):
        left = max(left, block[j])
    for j in range(i, w):
        right = max(right, block[j])
    water += min(left, right) - block[i]

print(water)