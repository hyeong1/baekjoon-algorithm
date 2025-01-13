list = []
total = 0
for i in range(5):
    n = int(input())
    list.append(n)
    total += n
list.sort()
print(total // 5)
print(list[2])
