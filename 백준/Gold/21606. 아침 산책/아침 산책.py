import sys
sys.setrecursionlimit(10**6)


def dfs(node, count):
    visited[node] = 1
    for adj in graph[node]:
        if is_inside[adj] == 1:
            count += 1
        elif visited[adj] == 0:
            count = dfs(adj, count)
    return count


N = int(input())
state = input()
is_inside = []
visited = [0] * N
for i in state:
    is_inside.append(int(i))

graph = [[] for _ in range(N)]
answer = 0
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
    if is_inside[u-1] == is_inside[v-1] == 1:
        answer += 2

path = 0
for i in range(N):
    if is_inside[i] == 1 and visited[i] == 0:
        x = dfs(i, 0)
        path += x * (x-1)

print(path + answer)