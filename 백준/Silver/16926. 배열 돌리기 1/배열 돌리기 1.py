from sys import stdin

# 입력 받기
N, M, R = map(int, stdin.readline().split())
matrix = [list(map(int, stdin.readline().split())) for _ in range(N)]

# 회전 함수 정의
def rotate_layer(layer):
    rotated = layer[R % len(layer):] + layer[:R % len(layer)]
    return rotated

# 행렬 회전 및 결과 출력
for layer in range(min(N, M) // 2):
    row, col = N - 2 * layer, M - 2 * layer
    temp = []

    # 윗면
    for c in range(col):
        temp.append(matrix[layer][layer + c])

    # 오른쪽면
    for r in range(1, row - 1):
        temp.append(matrix[layer + r][layer + col - 1])

    # 아랫면
    for c in range(col - 1, -1, -1):
        temp.append(matrix[layer + row - 1][layer + c])

    # 왼쪽면
    for r in range(row - 2, 0, -1):
        temp.append(matrix[layer + r][layer])

    # 레이어 회전 및 결과 적용
    temp = rotate_layer(temp)
    idx = 0
    # 윗면
    for c in range(col):
        matrix[layer][layer + c] = temp[idx]
        idx += 1

    # 오른쪽면
    for r in range(1, row - 1):
        matrix[layer + r][layer + col - 1] = temp[idx]
        idx += 1

    # 아랫면
    for c in range(col - 1, -1, -1):
        matrix[layer + row - 1][layer + c] = temp[idx]
        idx += 1

    # 왼쪽면
    for r in range(row - 2, 0, -1):
        matrix[layer + r][layer] = temp[idx]
        idx += 1

# 결과 출력
for row in matrix:
    print(*row)