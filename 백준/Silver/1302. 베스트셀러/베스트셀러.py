n = int(input())
books = {}
for _ in range(n):
    b = input()
    if b not in books:
        books[b] = 1
    else:
        books[b] += 1

_max = -1
_max_key = ''
for k in sorted(books.keys()):
    if _max < books[k]:
        _max = books[k]
        _max_key = k

print(_max_key)