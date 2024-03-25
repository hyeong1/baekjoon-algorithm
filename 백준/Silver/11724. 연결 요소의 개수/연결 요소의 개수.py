import sys
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v] = graph[v][u] = True


def dfs(node):
    global visited

    if visited[node]:
        return
    visited[node] = True
    for j in range(1, N+1):
        if not visited[j] and graph[node][j]:
            dfs(j)


result = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        result += 1

print(result)
