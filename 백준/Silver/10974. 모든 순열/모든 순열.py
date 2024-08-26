from itertools import permutations

n = int(input())
all_nums = []
for i in range(n):
    all_nums.append(i+1)

for all_case in permutations(all_nums, n):
    for a in all_case:
        print(a, end=" ")
    print()
