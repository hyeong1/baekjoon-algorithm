import heapq

N = int(input())
heap = []
for _ in range(N):
    heap.append(int(input()))

heapq.heapify(heap)
result = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    result += a + b
    heapq.heappush(heap, a + b)

print(result)
