N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
for i in range(N):
    tmp = max(B) * min(A)
    B.remove(max(B))
    A.remove(min(A))
    answer += tmp

print(answer)
