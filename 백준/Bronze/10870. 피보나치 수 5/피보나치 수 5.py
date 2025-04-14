def fibo(m):
    if m == 0:
        return 0
    if m == 1:
        return 1
    return fibo(m-1) + fibo(m-2)


n = int(input())
print(fibo(n))