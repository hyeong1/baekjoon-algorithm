import sys

N, K = map(int, sys.stdin.readline().split())

digit = 1
while digit * (10 ** (digit - 1)) * 9 < K:  # 필요 없는 개수 없애는 과정
    K -= digit * (10 ** (digit - 1)) * 9
    digit += 1

number = 10 ** (digit - 1) + (K - 1) // digit
if number > N:
    print(-1)
else:
    print(str(number)[(K-1) % digit])
