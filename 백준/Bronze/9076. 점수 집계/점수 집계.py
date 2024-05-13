T = int(input())

for _ in range(T):
    score = list(map(int, input().split()))

    score.remove(min(score))
    score.remove(max(score))

    min_s, max_s = min(score), max(score)
    if max_s - min_s >= 4:
        print("KIN")
    else:
        print(sum(score))
