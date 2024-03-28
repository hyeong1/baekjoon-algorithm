N = int(input())
two_before = 1
one_before = 2

answer = 0
for _ in range(3, N+1):
    answer = (two_before + one_before) % 15746
    two_before = one_before
    one_before = answer

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    print(answer)
