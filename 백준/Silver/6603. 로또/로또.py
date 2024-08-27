import sys


def dfs(start, all_case, k_list):
    if len(all_case) == 6:
        print(" ".join(map(str, all_case)))
        return
    for i in range(start, k):
        all_case.append(k_list[i])
        dfs(i+1, all_case, k_list)
        all_case.pop()


k = 1
while k != 0:
    k_list = list(map(int, sys.stdin.readline().split()))
    k = k_list[0]
    k_list = k_list[1:]
    dfs(0, [], k_list)
    print()


