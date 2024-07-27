n = int(input())
s = input()
res = 0
num = []

def get_hidden_num(num):
    hidden_num = ''.join(num)
    return int(hidden_num)

if not s.isalpha():
    for i in range(n):
        if s[i].isdigit():
            num.append(s[i])
            if i == n - 1:
                res += get_hidden_num(num)
                num = []
        elif num:
            res += get_hidden_num(num)
            num = []

print(res)
