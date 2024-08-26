import sys
from itertools import combinations

N, K = map(int, sys.stdin.readline().split())


def sol(N, K):
    if K < 5:
        return 0
    
    ans = 0
    words_set = set()
    unique_list = []
    for _ in range(N):
        now = set(sys.stdin.readline().rstrip())
        now_cnt = len(now)
        if now_cnt == 5:
            ans += 1
            continue
        now_unique = now - {'a', 'n', 't', 'i', 'c'}
        unique_list.append(now_unique)
        words_set = words_set.union(now_unique)

    if len(unique_list) == 0:
        return ans
    if len(words_set) <= K-5:
        return ans + len(unique_list)

    max_cnt = 0
    for case in combinations(words_set, K-5):
        case_cnt = 0
        case_set = set(case)
        for word_set in unique_list:
            if word_set.issubset(case_set):
                case_cnt += 1
        max_cnt = max(max_cnt, case_cnt)
    ans += max_cnt
    return ans


print(sol(N, K))
