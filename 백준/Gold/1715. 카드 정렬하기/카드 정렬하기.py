import heapq

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))

result = 0
while True:
    a = heapq.heappop(heap)
    if not heap:
        break
    b = heapq.heappop(heap)
    tmp = a + b
    result += tmp
    heapq.heappush(heap, tmp)

print(result)
