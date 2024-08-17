from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
all_case = list(combinations(cards, 3))
result = []

for case in all_case:
    if sum(case) <= m:
        result.append(sum(case))

print(max(result))