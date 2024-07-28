import heapq

len_a, len_b = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

heap = []
for n in a:
    heapq.heappush(heap, n)
for n in b:
    heapq.heappush(heap, n)

for _ in range(len_a + len_b):
    print(heapq.heappop(heap), end=' ')