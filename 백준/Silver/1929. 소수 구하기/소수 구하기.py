def isPrime(num):
    if num == 2 or num ==3:
        return True
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True


n, m = map(int, input().split(" "))
if n == 1:
    n += 1
for i in range(n, m+1):
    if isPrime(i):
        print(i)