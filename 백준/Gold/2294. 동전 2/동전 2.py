import sys

N, K = map(int, input().split())
coins = list(set(int(sys.stdin.readline()) for _ in range(N)))
check = [0 for _ in range(K+1)]  # K원을 만드는 데 사용된 동전 개수 배열


def solve():
    if K == 0:
        print(0)
        sys.exit()

    prev = [0]
    current = []
    nc = 0
    visited = [False] * (K+1)
    visited[0] = True
    while prev:
        nc += 1
        for v in prev:
            for c in coins:
                new_val = v + c
                if new_val == K:
                    return nc
                elif new_val > K:
                    continue
                elif not visited[new_val]:
                    visited[new_val] = True
                    current.append(new_val)
        prev, current = current, []
    return -1


print(solve())