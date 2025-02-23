import sys
sys.setrecursionlimit(100000)

t = int(input())


def dfs(r, c):
    for rr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
        if cc < 0 or cc > m-1 or rr < 0 or rr > n-1:
            continue
        if graph[rr][cc] == 1 and not visited[rr][cc]:
            visited[rr][cc] = True
            dfs(rr, cc)


for _ in range(t):
    m, n, k = map(int, input().split(" "))
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    ans = 0

    for _ in range(k):
        X, Y = map(int, input().split(" "))
        graph[Y][X] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)
                ans += 1
    print(ans)